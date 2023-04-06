from django.core.mail import send_mail

# activation send code
# def send_confirmation_email(user, code):
#     send_mail(
#         'Здравствуйте, активируйте ваш аккаунт',
#         f'Чтобы активировать аккаунт надо ввести код:'
#         f'\n{code}'
#         f'\nНе передавайте этот код никому!',
#         'xorysteam.dev@gmail.com',
#         [user],
#         fail_silently=False,
#     )


# activation send link
def send_confirmation_email(user, code):
    full_link = f'http://localhost:8000/api/v1/accounts/activate/{code}'
    send_mail(
        'Здравствуйте, активируйте ваш аккаунт',
        f'Чтобы активировать аккаунт, нужно перейти по ссылке:'
        f'\n{full_link}'
        f'\nНе передавайте ссылку никому!',
        'xorysteam.dev@gmail.com',
        [user],
        fail_silently=False,
    )