from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMessage


# def envio_email(title, data, dest_list):
#
#     title_email = '%s %s' % (settings.EMAIL_SUBJECT_PREFIX, title)
#
#     template = get_template('01_base/email/email.html').render(data)
#
#     msg = EmailMessage(
#         title_email,
#         template,
#         settings.EMAIL_HOST_USER,
#         dest_list,
#     )
#     msg.content_subtype = "html"  # O conteúdo principal agora está em text/html
#     msg.send()


def envio_email(nome, email_destino):
    assunto = 'Bem-vindo ao Nosso Sistema'
    mensagem = f'Olá {nome},\n\nBem-vindo ao nosso sistema! Esperamos que você aproveite a sua estadia.'
    remetente = 'recicalgem.mori@gmail.com'  # Seu endereço de email
    destinatarios = [email_destino]

    send_mail(assunto, mensagem, remetente, destinatarios, fail_silently=False)
