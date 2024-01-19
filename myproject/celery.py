# celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
from datetime import timedelta

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Create a Celery instance and configure it using the settings from Django.
app = Celery('myproject')

# Load task modules from all registered Django app configs.
app.config_from_object(settings, namespace='CELERY')

# Auto-discover tasks in all installed apps
app.autodiscover_tasks()

# Schedule the task to run every day at a specific time (e.g., midnight)
app.conf.beat_schedule = {
    'send-expiry-reminder-emails': {
        'task': 'celery_app.tasks.send_expiry_reminder_emails',
        'schedule': crontab(hour=6, minute=0),
    },
    'print-hello': {
        'task': 'celery_app.tasks.print_hello',
        'schedule': timedelta(seconds=5),  # Run every minute
    },
}