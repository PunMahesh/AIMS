from django.core.mail import send_mail
import uuid


def send_forget_password(email):
    token = str(uuid.uuid4())
    subject = "Your forget Password Link"
    message = f"Hi, Click on the link to reset your password"

