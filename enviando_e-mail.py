#enviando E-mail SMTP com Python
import os
import pathlib
from string import Template
from dotenv import load_dotenv #type: ignore
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

load_dotenv()

#Caminho HTML
CAMINHO_HTML = pathlib.Path(__file__).parent / 'email.html'

# Dados do remetente e destinatario
remetente = os.getenv('FROM_EMAIL','')
destinatario = remetente

#Configuracoes SMTP

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = os.getenv('FROM_EMAIL','')
smtp_password = os.getenv('EMAIL_PASSWORD','')

#mensagem de Texto
with open(CAMINHO_HTML,'r')as arquivo:
    texto_arquivo = arquivo.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(nome = 'João')


#Transformar mensagem em MIMEMultipart

mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Este é o assunto'

corpo_email = MIMEText(texto_email,'html','utf-8')
mime_multipart.attach(corpo_email)

#envia o e-mail
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.send_message(mime_multipart)
    print('email enviado com sucessos')