#!/bin/bash
echo "Arguments received: $@"

if [ "$1" = "runapp" ]; then
    echo "Running migrations..."
    python manage.py makemigrations
    python manage.py migrate

    echo "Checking for superuser existence and creating if not found..."
    python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
EOF

    echo "Starting Gunicorn..."
    exec gunicorn config.wsgi:application --bind 0.0.0.0:8080 --workers 3 --timeout 300 --log-level debug
else
    echo "Unknown argument: $1"
    echo "Usage: $0 runapp"
    exit 1
fi
