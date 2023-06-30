from django.conf import settings
from django.core.mail import send_mail


def send_register_email(email):
    send_mail(
        subject='Поздравляем с регистрацией',
        message='Вы зарегистрировались на нашей платформе, добро пожаловать!',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
        # recipient_list=[new_user.email]
    )


def send_new_password(email, new_password):
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )
