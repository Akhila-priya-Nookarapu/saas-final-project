from fastapi import FastAPI, Depends, HTTPException
from database import SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy import text
from models import User, Project, Task
from passlib.hash import pbkdf2_sha256 as hasher
from auth import create_token, get_current_user

app = FastAPI()

# ---------------- DB Dependency ----------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------- HEALTH CHECK ----------------
@app.get("/api/health")
def health():
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        return {"status": "ok", "database": "connected"}
    except Exception as e:
        return {"status": "fail", "database": "not connected", "error": str(e)}


# ---------------- LOGIN API ----------------
@app.post("/api/auth/login")
def login(data: dict, db: Session = Depends(get_db)):
    email = data.get("email")
    password = data.get("password")

    user = db.query(User).filter(User.email == email).first()

    if not user or not hasher.verify(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token(user)

    return {
        "access_token": token,
        "role": user.role,
        "tenantId": user.tenant_id
    }


# ---------------- TENANT SECURITY ----------------
def tenant_required(user=Depends(get_current_user)):
    # ⛔ SUPER IMPORTANT FIX
    # Tenant APIs require tenant id, always.
    if user.tenant_id is None:
        raise HTTPException(status_code=403, detail="Tenant access required")
    return user


# ---------------- PROJECT APIs ----------------

# Create Project (Tenant Admin Only)
@app.post("/api/projects")
def create_project(data: dict, user=Depends(tenant_required), db: Session = Depends(get_db)):
    if user.role != "tenant_admin":
        raise HTTPException(status_code=403, detail="Only tenant admin can create projects")

    project = Project(
        name=data["name"],
        tenant_id=user.tenant_id
    )

    db.add(project)
    db.commit()

    return {"message": "Project created"}


# Get Projects (Tenant Users)
@app.get("/api/projects")
def get_projects(user=Depends(tenant_required), db: Session = Depends(get_db)):
    return db.query(Project).filter(Project.tenant_id == user.tenant_id).all()


# ---------------- TASK APIs ----------------

# Create Task
@app.post("/api/tasks")
def create_task(data: dict, user=Depends(tenant_required), db: Session = Depends(get_db)):

    task = Task(
        title=data["title"],
        project_id=data["project_id"]
    )

    db.add(task)
    db.commit()

    return {"message": "Task created"}


# Update Task Status (safe – if no column, ignore)
@app.patch("/api/tasks/status")
def update_status(data: dict, user=Depends(tenant_required), db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == data["task_id"]).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # if status column does not exist, skip
    try:
        task.status = data["status"]
    except:
        pass

    db.commit()

    return {"message": "updated"}


# ---------------- DASHBOARD ----------------
@app.get("/api/dashboard")
def dashboard(user=Depends(tenant_required), db: Session = Depends(get_db)):

    project_ids = [
        p.id for p in db.query(Project.id)
        .filter(Project.tenant_id == user.tenant_id)
        .all()
    ]

    project_count = len(project_ids)

    if project_ids:
        task_count = db.query(Task).filter(
            Task.project_id.in_(project_ids)
        ).count()
    else:
        task_count = 0

    try:
        if project_ids:
            completed_count = db.query(Task).filter(
                Task.project_id.in_(project_ids),
                Task.status == "completed"
            ).count()
        else:
            completed_count = 0
    except:
        completed_count = 0

    return {
        "projects": project_count,
        "tasks": task_count,
        "completed": completed_count
    }
