# AI-Powered Student Performance Tracker API

## Project Overview
The AI-Powered Student Performance Tracker is a backend REST API designed to help university students and lecturers track academic performance, identify risks early, and provide timely reminders for improvement.

The system automatically analyzes student assessment marks and assigns performance statuses such as *Excellent*, *Good*, *At Risk*, or *Failing*. This logic simulates AI-driven decision-making without relying on external machine learning libraries, making it lightweight, explainable, and suitable for academic environments.

## Problem Statement
Many university students fail courses not because of lack of ability, but due to poor performance tracking, late awareness of academic risk, and lack of reminders.

This project addresses that gap by:
- Tracking student assessments
- Automatically identifying performance risk
- Providing reminders to guide improvement
- Enforcing role-based access for students and lecturers


## Key Features
- User authentication (students & lecturers)
- Role-based access control
- Unit (course) management
- Assessment tracking with automatic performance evaluation
- Reminder system for academic tasks
- Secure RESTful API
- AI-inspired performance logic


## AI-Powered Logic 
The system uses rule-based intelligence to simulate AI behavior.

Based on assessment marks:
- 70 – 100 → Excellent
- 60 – 69 → Good
- 40 – 59 → At Risk
- Below 40 → Failing

Performance status is automatically generated when assessments are created or updated.

No human manually sets the status — the system decides.


## Technology Stack
- Python
- Django
- Django REST Framework
- SQLite (development)
- JWT Authentication (optional extension)


## Project Structure

student_tracker/
├── student_tracker_project/
│ ├── settings.py
│ ├── urls.py
│
├── student_tracker_app/
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── urls.py
│
├── manage.py
└── README.md


## API Endpoints

### Authentication
| Method | Endpoint | Description |
|------|--------|------------|
| POST | /auth/login/ | Login user |
| POST | /auth/register/ | Register user |

### Units
| Method | Endpoint | Description |
|------|--------|------------|
| GET | /units/ | List units |
| POST | /units/ | Create unit |
| PUT | /units/{id}/ | Update unit |
| DELETE | /units/{id}/ | Delete unit |

### Assessments
| Method | Endpoint | Description |
|------|--------|------------|
| GET | /assessments/ | List assessments |
| POST | /assessments/ | Create assessment |
| PUT | /assessments/{id}/ | Update assessment |
| DELETE | /assessments/{id}/ | Delete assessment |

### Reminders
| Method | Endpoint | Description |
|------|--------|------------|
| GET | /reminders/ | List reminders |
| POST | /reminders/ | Create reminder |
| PUT | /reminders/{id}/ | Update reminder |
| DELETE | /reminders/{id}/ | Delete reminder |



## How to Run the Project Locally

1. Clone the repository
```bash
git clone <repo-url>
cd Student_performance_tracker_api


Create virtual environment

python -m venv venv
source venv/Scripts/activate


Install dependencies

pip install -r requirements.txt


Run migrations

python manage.py migrate


Create superuser

python manage.py createsuperuser


Run server

python manage.py runserver

Testing the API:

The API can be tested using:

Django REST Framework browsable API

Admin panel

Postman (optional)

Students can only view their own data, while lecturers have broader access.

Future Improvements;

Email notifications

Performance trend analytics

Recommendation engine for study resources

Frontend dashboard

Author

Hope Faith Awuor
Backend Developer
