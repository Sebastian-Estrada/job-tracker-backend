# Use a smaller base image with Python
FROM python:3.12.5-slim

# Install dependencies and generate the locale
RUN apt-get update && \
    apt-get install -y nginx

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy requirements early to leverage Docker cache
COPY requirements.txt /tmp/requirements.txt

# Install Python dependencies without caching
RUN pip install --no-cache-dir -r /tmp/requirements.txt && \
    pip install --no-cache-dir gunicorn

# Copy application code
COPY .  /var/www/html/job-tracker-backend

# Set the working directory
WORKDIR /var/www/html/job-tracker-backend
# Collect static files
RUN python manage.py collectstatic

# Prepare configuration files
# RUN cp ./nginx/000-backend.conf /etc/nginx/sites-enabled/ && \ 
# cp ./nginx/proxy_params /etc/nginx/ && \ 
# cp ./nginx/wsgi_params /etc/nginx/ && \ 
# cp ./nginx/nginx.conf /etc/nginx/ && \
# rm -f /etc/nginx/sites-enabled/default && \
RUN sed -i -e 's/\r$//' ./Docker/entrypoint.sh && \
chmod +x ./Docker/entrypoint.sh && \
chmod +x manage.py

# Set entrypoint
ENTRYPOINT ["./Docker/entrypoint.sh"]

CMD ["runapp"]