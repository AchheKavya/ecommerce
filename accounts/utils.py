from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings

from .tokens import email_verification_token


def send_verification_email(user, request):
    token = email_verification_token.make_token(user)
    uid = user.pk

    verification_link = request.build_absolute_uri(
        reverse('verify_email', args=[uid, token])
    )

    subject = "Confirm your E-Shop account"
    message = f"""
Hi {user.username},

Thank you for registering on E-Shop.

Please click the link below to verify your email address:

{verification_link}

If you did not create this account, you can ignore this email.
"""

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
    )
