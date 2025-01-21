# Job Tracker Backend

## Problem Description

Job hunting can be a tedious and overwhelming process. Keeping track of job applications, follow-ups, and responses from potential employers can quickly become unmanageable. This project aims to simplify and streamline the job application process by providing a centralized platform to track and manage job applications.

## Project Description

The Job Tracker is a web application designed to help users manage their job applications efficiently. Users can add new job applications, update the status of their applications, and set reminders for follow-ups. The application provides a user-friendly interface to view and manage all job-related activities in one place.

## Project Technology Stack

- **Backend:**
    - Django
    - Django REST Framework (DRF)

- **Database:**
    - PostgreSQL

- **Other Tools and Libraries:**
    - Docker for containerization
    - pytest for testing

## Installation and Configuration

### Prerequisites

- Docker and Docker Compose installed on your machine
- Python 3.8 or higher
- PostgreSQL

### Steps

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/job_tracker.git
    cd job_tracker/backend
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the PostgreSQL database:**
    - Create a new PostgreSQL database and user.
    - Update the `DATABASES` setting in `settings.py` with your database credentials.

5. **Run database migrations:**
    ```bash
    python manage.py migrate
    ```

6. **Start the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Run the application using Docker:**
    ```bash
    docker-compose up --build
    ```

8. **Run tests:**
    ```bash
    pytest
    ```

Now, you should be able to access the application at `http://localhost:8000`.

