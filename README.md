# 🛠️ Django Project Management API
This is a RESTful API built with Django and Django REST Framework to manage users, projects, tasks, comments, and audit logs. It supports full CRUD operations, user registration and login, and provides endpoints to track project activities.

## 🚀 Features
- User Registration and Authentication
- Project Management (Add, View, Edit, Delete)
- Task Management (Add, View, Edit, Delete)
- Commenting System (Add, View, Edit, Delete)
- Audit Logs (Add, View, Edit, Delete)
- Clean and structured error handling
- API responses are consistent and informative

## 📁 Project Structure
project_root/
├── models.py
├── views.py
├── serializers.py
├── urls.py
├── settings.py
└── ...

## 📡 API Endpoints
🔐 Authentication
| Method | Endpoint     | Description         |
| ------ | ------------ | ------------------- |
| POST   | `/register/` | Register a new user |
| POST   | `/login/`    | Log in a user       |
| GET    | `/logout/`   | Log out the user    |


📁 Projects
| Method | Endpoint          | Description          |
| ------ | ----------------- | -------------------- |
| POST   | `/projects/`      | Create a new project |
| GET    | `/projects/`      | Get all projects     |
| GET    | `/projects/<id>/` | Get a single project |
| PUT    | `/projects/<id>/` | Edit a project       |
| DELETE | `/projects/<id>/` | Delete a project     |

✅ Tasks
| Method | Endpoint       | Description       |
| ------ | -------------- | ----------------- |
| POST   | `/tasks/`      | Create a new task |
| GET    | `/tasks/`      | Get all tasks     |
| GET    | `/tasks/<id>/` | Get a single task |
| PUT    | `/tasks/<id>/` | Edit a task       |
| DELETE | `/tasks/<id>/` | Delete a task     |

💬 Comments
| Method | Endpoint          | Description          |
| ------ | ----------------- | -------------------- |
| POST   | `/comments/`      | Add a comment        |
| GET    | `/comments/`      | Get all comments     |
| GET    | `/comments/<id>/` | Get a single comment |
| PUT    | `/comments/<id>/` | Edit a comment       |
| DELETE | `/comments/<id>/` | Delete a comment     |

📝 Audit Logs
| Method | Endpoint           | Description              |
| ------ | ------------------ | ------------------------ |
| POST   | `/auditlogs/`      | Add a new audit log      |
| GET    | `/auditlogs/`      | Get all audit logs       |
| GET    | `/auditlogs/<id>/` | Get a specific audit log |
| PUT    | `/auditlogs/<id>/` | Edit an audit log        |
| DELETE | `/auditlogs/<id>/` | Delete an audit log      |

## 📌 Notes
- Be sure to add appropriate authentication/authorization before using this in production.
- Consider using DRF ViewSets and Routers to reduce boilerplate code.
- Extend the AuditLog to automatically track changes using Django signals or middleware.

