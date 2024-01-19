# your_app/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from datetime import datetime, timedelta
from .models import SoftwareDetails

@shared_task
def send_expiry_reminder_emails():
    # Calculate the date one month ago
    one_month_ago = datetime.now() - timedelta(days=30)

    # Retrieve items with expiry date within the last month
    items_to_remind = SoftwareDetails.objects.filter(expiry_date__gte=one_month_ago, expiry_date__lte=datetime.now())

    for item in items_to_remind:
        subject = 'Expiry Reminder'
        message = f"Dear user, the expiry date for {item.descriptions} is approaching on {item.expiry_date}."
        from_email = 'miteshtiwary@example.com'
        recipient_list = [item.email_address]

        send_mail(subject, message, from_email, recipient_list)


@shared_task
def print_hello():
    print("Hello")