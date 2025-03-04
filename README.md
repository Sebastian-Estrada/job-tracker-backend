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

### Configuration of env

1. **Configure the environment variables:**

Create a `.env` file in the root directory of your project and add the following environment variables:

    # Security
    SECRET_KEY=secret_key
    DEBUG=True
    # Database
    DB_NAME=db_name
    DB_USER=postgres
    DB_PASSWORD=password
    DB_HOST=host.docker.internal
    DB_PORT=5432
    # Django Settings
    ALLOWED_HOSTS=localhost,127.0.0.1, job-tracker-backend, job-tracker-frontend
    # Other settings
    CORS_ALLOWED_ORIGINS=http://job-tracker-frontend:5173

### Configuration of project

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
    - Create a `.env` file and add the necessary environment variables.
    - Update the `DATABASES` setting in `.env` with your database credentials.

5. **Run database migrations:**
    ```bash
    python manage.py migrate
    ```

6. **Start the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Build the Docker image for the backend:**
    ```bash
    docker build -f Docker/Dockerfile -t job-tracker-backend .
    ```

8. **Run the application using Docker:**
    ```bash
    docker compose -f .\Docker\docker-compose.yaml up
    ```

9. **Run tests:**
    ```bash
    pytest
    ```

Now, you should be able to access the application at `http://localhost:8080`.

## Docker and AWS ECR Deployment Instructions

This section provides the steps to build, tag, and push a Docker image to AWS Elastic Container Registry (ECR).

1. **Build the Docker Image**:
    - Use the Dockerfile located in the `Docker` directory to build the Docker image.
    - Tag the image as `backend`.

    ```sh
    docker build -f Docker/Dockerfile -t backend .
    ```

2. **Tag the Docker Image**:
    - Tag the Docker image with the ECR repository URI.

    ```sh
    docker tag backend:latest 732978450718.dkr.ecr.ca-central-1.amazonaws.com/backend:latest
    ```

3. **Authenticate Docker to AWS ECR**:
    - Use the AWS CLI to get the ECR login password and authenticate Docker to your ECR registry.
    - Ensure you are using the correct AWS profile and region.

    ```sh
    aws ecr get-login-password --region ca-central-1 --profile personal-account | docker login --username AWS --password-stdin 732978450718.dkr.ecr.ca-central-1.amazonaws.com
    ```

4. **Push the Docker Image to ECR**:
    - Push the tagged Docker image to the specified ECR repository.

    ```sh
    docker push 732978450718.dkr.ecr.ca-central-1.amazonaws.com/backend:latest
    ```

<!-- docker build -f Docker/Dockerfile -t backend .
docker tag backend:latest 732978450718.dkr.ecr.ca-central-1.amazonaws.com/backend:latest
aws ecr get-login-password --region ca-central-1 --profile personal-account | docker login --username AWS --password-stdin 732978450718.dkr.ecr.ca-central-1.amazonaws.com
docker push 732978450718.dkr.ecr.ca-central-1.amazonaws.com/backend:latest -->