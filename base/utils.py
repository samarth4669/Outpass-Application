from django.core.mail import send_mail

from django.conf import settings


def sendemail(email,subject,message):
    
    send_mail(
      subject,
      message,
      settings.EMAIL_HOST_USER,
      [email],
      fail_silently=False
    )