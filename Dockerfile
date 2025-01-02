# Use Python 3.12 Alpine as the base image
FROM python:3.12-alpine

# Set environment variables to avoid buffer issues
ENV PYTHONUNBUFFERED=1

# Install necessary system dependencies
RUN apk add --no-cache \
	cronie \
    && pip install --upgrade pip \
    && pip install psycopg2-binary

# Set working directory inside the container
WORKDIR /app

COPY backup.py backup.py
COPY beds.py beds.py
COPY csv_access.py csv_access.py
COPY database_access.py database_access.py
COPY day_emergencies.py day_emergencies.py
COPY day_vitals.py day_vitals.py
COPY procedures.py procedures.py
COPY staff.py staff.py
COPY env.json env.json

# Copy crontab file if needed (optional)
#COPY my-cronjob /etc/cron.d/my-cronjob

# Set permissions and apply crontab
#RUN chmod 0644 /etc/cron.d/my-cronjob && \
#    crontab /etc/cron.d/my-cronjob && \
#    touch /var/log/cron.log

# Expose ports if necessary (optional)
#EXPOSE 8000

# Start both cron and the Python app
CMD ["sh", "-c", "python staff.py"]