from database import SessionLocal
from models import *
from passlib.hash import pbkdf2_sha256 as hasher


db = SessionLocal()

if db.query(User).count() == 0:
    super_admin = User(
        email="superadmin@system.com",
        password=hasher.hash("Admin@123"),
        role="super_admin",
        tenant_id=None
    )

    tenant = Tenant(name="Demo Company", subdomain="demo", status="active")
    db.add(tenant)
    db.flush()

    admin = User(
        email="admin@demo.com",
        password=hasher.hash("Demo@123"),
        role="tenant_admin",
        tenant_id=tenant.id
    )

    user1 = User(email="user1@demo.com", password=hasher.hash("User@123"), role="user", tenant_id=tenant.id)
    user2 = User(email="user2@demo.com", password=hasher.hash("User@123"), role="user", tenant_id=tenant.id)

    project = Project(name="Project Alpha", tenant_id=tenant.id)
    db.add_all([super_admin, admin, user1, user2, project])
    db.commit()

print("Seeding complete")
