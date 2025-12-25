📌 SaaS Multi-Tenant Project – Final Submission

This project is a SaaS style multi-tenant application where each tenant (organization) has its own projects, tasks and users.
It supports authentication, authorization, tenant isolation, secure APIs and runs completely using Docker.

✅ Features Implemented
🔐 Authentication & Authorization

Login using email + password

JWT-based authentication

Roles supported:

super_admin

tenant_admin

tenant_user

Secure protected routes

🏢 Multi-Tenant Architecture

Each user belongs to a tenant

Tenant users can access only their data

Super Admin cannot access tenant APIs
(returns 403 Tenant access required) ✔️

📂 Project & Task Management

Tenant Admin can create projects

Users of tenant can view projects

Tasks can be created under projects

Dashboard shows:

Number of projects

Number of tasks

Number of completed tasks

🩺 Health Check

Confirms system and database connection:

/api/health

🐳 Dockerized Application

Runs using:

docker-compose up -d --build


Containers:

PostgreSQL Database

Backend (FastAPI)

Frontend

All services start automatically.

👤 Seeded Users (Default Login Credentials)
Role	Email	Password
Super Admin	superadmin@system.com
	Admin@123
Tenant Admin	admin@demo.com
	Demo@123
Tenant User	user1@demo.com
	User@123
🧪 Tested & Verified APIs
🔹 Authentication
POST /api/auth/login

🔹 Projects
GET /api/projects
POST /api/projects   (Tenant Admin only)

🔹 Tasks
POST /api/tasks

🔹 Dashboard
GET /api/dashboard

🔹 Health
GET /api/health

🔒 Tenant Security Proof

Tenant Admin → Can access tenant projects

Tenant User → Can access tenant projects

Super Admin → Forbidden (403) ✔️
Ensures strong tenant isolation.

🎥 Demo Video Flow

1️⃣ Start containers
2️⃣ Show health check working
3️⃣ Login as Tenant Admin
4️⃣ Show projects
5️⃣ Create task
6️⃣ Show dashboard update
7️⃣ Login as normal user
8️⃣ Login as Super Admin → show 403 Forbidden

🏁 Final Status

✔️ All APIs working
✔️ Authentication working
✔️ Tenant isolation implemented
✔️ Dashboard functional
✔️ Docker working
✔️ Ready for evaluation 🎯

🙌 Author

Akhila Priya Nookarapu
