# 📌 SaaS Multi-Tenant Project – Final Submission

This project is a **SaaS style multi-tenant application** where each tenant (organization) has its own projects, tasks and users.  
It supports authentication, authorization, tenant isolation, secure APIs and runs completely using Docker.

---

## ✅ Features Implemented

### 🔐 Authentication & Authorization
- Login using email + password  
- JWT-based authentication  
- User roles:
  - **super_admin**
  - **tenant_admin**
  - **tenant_user**
- Secure protected APIs

---

### 🏢 Multi-Tenant Architecture
- Each user belongs to a tenant  
- Tenant users can access only their data  
- **Super Admin cannot access tenant APIs**  
  (returns `403 Tenant access required`) ✔️

---

### 📂 Project & Task Management
- Tenant Admin can create projects  
- Users of tenant can view projects  
- Tasks can be created under projects  
- Dashboard shows:
  - Total Projects
  - Total Tasks
  - Completed Tasks

---

## 🩺 Health Check
Confirms system and database connection:
GET /api/health

---

## 🐳 Dockerized Application
Run the project using:

docker-compose up -d --build

Services included:
- PostgreSQL Database  
- FastAPI Backend  
- Frontend UI  

All containers start automatically.

---

## 👤 Seeded Users (Login Credentials)

| Role          | Email                     | Password  |
|--------------|---------------------------|----------|
| Super Admin  | superadmin@system.com     | Admin@123 |
| Tenant Admin | admin@demo.com            | Demo@123  |
| Tenant User  | user1@demo.com            | User@123  |

---

## 🧪 Verified APIs

### Authentication
POST /api/auth/login


### Projects
GET /api/projects
POST /api/projects (Tenant Admin only)

### Tasks
POST /api/tasks

### Dashboard
GET /api/dashboard


### Health
GET /api/health


---

## 🔒 Tenant Security Proof
- Tenant Admin → Access tenant data  
- Tenant User → Access tenant data  
- **Super Admin → Blocked from tenant APIs with 403** ✔️

Ensures full tenant isolation.

---

## 🎥 Demo Flow
1️⃣ Start containers  
2️⃣ Health Check  
3️⃣ Login tenant admin  
4️⃣ View + create projects  
5️⃣ Create task  
6️⃣ Dashboard updates  
7️⃣ Login normal user  
8️⃣ Login super admin → show 403 Forbidden


## 🎥 Demo Video
Watch here:
https://drive.google.com/file/d/1B8cTRFYsDeas3e0HmtGlNf7F8wzKgtqW/view?usp=sharing
---

## 🏁 Final Status
✔️ Authentication working  
✔️ Tenant isolation working  
✔️ Dashboard functional  
✔️ Docker working  
✔️ APIs verified  
✔️ Ready for evaluation 🎯

---

## 🙌 Author
**Akhila Priya Nookarapu**
