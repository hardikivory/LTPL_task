import uuid

from .models import User
from django.core.mail import EmailMessage


def otp_gen():
    return uuid.uuid4().hex[:6]


def send_email(data):
    email = EmailMessage(
    subject= data['subject'],
    body= data['message'],
    from_email= data['from_email'],
    to= [data['to_email']],)
    
    email.send()