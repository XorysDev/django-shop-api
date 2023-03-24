from django.core.mail import send_mail


def send_confirmation_email(user, code):
    send_mail(
        'Здравствуйте, активируйте ваш аккаунт',
        f'Чтобы активировать аккаунт надо ввести код:'
        f'\n{code}'
        f'\nНе передавайте этот код никому!',
        'xorysteam.dev@gmail.com',
        [user],
        fail_silently=False,
    )