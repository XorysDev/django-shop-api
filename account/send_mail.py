from django.core.mail import send_mail


def send_confirmation_email(user, code):
    send_mail(
        'Здравствуйте, активируйте ваш аккаунт',
        f'Чтобы активировать аккаунт надо ввести код:'
        f'{code}'
        f'Не передавайте этот код никому!'
        f'xorysteam.dev@gmail.com',
        [user], fail_silently=False,
    )