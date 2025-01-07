# Use Python 3.12 Alpine as the base image
FROM python:3.12-alpine

# Install necessary system dependencies
RUN apk add --no-cache postgresql\
	&& apk add --no-cache cronie \
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
COPY list.py list.py
COPY cronjob /etc/cron.d/cronjob

# Set permissions and apply crontab
RUN chmod 744 /app && \
    touch /var/log/cron-staff.log && \
	touch /var/log/cron-beds.log && \
	mkdir -p /app/reports && \
	crontab /etc/cron.d/cronjob

CMD ["crond", "-f", "-m off"]