from django.core.mail import send_mail

send_mail(
    subject='Teste Django',
    message='Funcionou!',
    from_email=None,  # usa DEFAULT_FROM_EMAIL
    recipient_list=['gustavo.rconceicao@aluno.senac.rio'],
    fail_silently=False,
)