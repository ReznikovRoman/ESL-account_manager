
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from email.message import EmailMessage


# Google API
# 913171329991-oqae5f99m07lo4g5ksni60b1qcs4ms6q.apps.googleusercontent.com
# XZybigE9ix_4VMu2_9fyZLwL

EMAIL_ADDRESS = 'esl.manager.mail@gmail.com'
EMAIL_PASSWORD = 'eslaccountmanagerdevop'


class EmailHandler:
    def __init__(self, setup_info):
        self.setup_info = setup_info
        self.email_address = get_email_from_file(self.setup_info)
        self.remember_me_state = get_remember_me_status(self.setup_info)

    def get_address(self):
        """Returns email address of an Admin/User."""
        return self.email_address

    def get_remember_me_state(self):
        """Returns 'True', if an Admin chose 'Remember Me' option; 'False' - in other cases."""
        return self.remember_me_state

    def normalize_email_content(self, msg_text):
        """'Normalizes' text (deletes all hrefs and '<a> </a>')."""

        tickets_link = ""
        match_link = ""

        regex_tickets = re.findall('Check your tickets: <a href=(.*)> ', msg_text)
        if len(regex_tickets) > 0:
            tickets_link = regex_tickets[0]
        regex_match = re.findall('Check match: <a href=(.*)> ', msg_text)
        if len(regex_match) > 0:
            match_link = regex_match[0]

        msg_text = re.sub('<a href=.*> Open protests </a>', tickets_link, msg_text)
        msg_text = re.sub('<a href=.*> Match page </a>', match_link, msg_text)
        return msg_text

    def send_email(self, msg_content):
        """"Sends email to the Admin/User."""
        msg = EmailMessage()
        msg['Subject'] = 'New protest'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = self.email_address
        # msg['To'] = 'salute...@staff.eslgaming.com'  # Test - Invalid email address
        msg_content = self.normalize_email_content(msg_content)
        msg.set_content(msg_content)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            try:
                smtp.send_message(msg)
            except Exception as e:
                # TODO: raise exception and print it to the screen
                return 'Email not found!'


def get_email_from_file(file_info):
    user_email = ""
    for value in file_info:
        email = re.findall('User email: (.*)', value)
        if len(email) != 0:
            user_email = email[0]
    return user_email


def get_send_email_status(file_info):
    send_email_status = True
    for value in file_info:
        if len(re.findall('Send email state: (.*)', value)) > 0:
            send_email_status = re.findall('Send email state: (.*)', value)[0]
            if send_email_status == '0':
                send_email_status = False
            elif send_email_status == '2':
                send_email_status = True
    return send_email_status


def get_remember_me_status(file_info):
    is_remember_me = False
    for value in file_info:
        remember_me = re.findall('\'Remember me\' status: (.*)', value)
        if len(remember_me) != 0:
            if remember_me[0] == '0':
                is_remember_me = False
            elif remember_me[0] == '2':
                is_remember_me = True
    return is_remember_me


def get_nickname(file_info):
    nickname = ""
    for value in file_info:
        nickname_list = re.findall('User nickname: (.*)', value)
        if len(nickname_list) != 0:
            nickname = nickname_list[0]
    return nickname


def get_error(file_info):
    error = False
    for value in file_info:
        error = re.findall('Error: (.*)', value)
        if len(error) != 0:
            if error[0] == '0':
                error = False
            elif error[0] == '1':
                error = True
    return error


def get_file_info():
    try:
        with open('setup_info.txt', 'r') as f:
            user_info = f.read().splitlines()
        return user_info
    except FileNotFoundError:
        return ["User email: ", "User nickname: ", "User password : ", "Send email state: ", "Is registered: ", "'Remember me' status: ", 'Error: 1']


# text_msg = 'Test message - 1\nTest message new row\nTest message url: https://google.com'
# EmailHandler(get_file_info()).send_email(text_msg)
# if EmailHandler(get_file_info()).send_email(text_msg) == 'Email not found!':
#     print('Alarm!!!')

# print(get_file_info())


'''
import smtplib                                      # Импортируем библиотеку по работе с SMTP

# Добавляем необходимые подклассы - MIME-типы
from email.mime.multipart import MIMEMultipart      # Многокомпонентный объект
from email.mime.text import MIMEText                # Текст/HTML
from email.mime.image import MIMEImage              # Изображения

addr_from = "from_address@mail.com"                 # Адресат
addr_to   = "to_address@mail.com"                   # Получатель
password  = "pass"                                  # Пароль

msg = MIMEMultipart()                               # Создаем сообщение
msg['From']    = addr_from                          # Адресат
msg['To']      = addr_to                            # Получатель
msg['Subject'] = 'Тема сообщения'                   # Тема сообщения

body = "Текст сообщения"
msg.attach(MIMEText(body, 'plain'))                 # Добавляем в сообщение текст

server = smtplib.SMTP('smtp-server', 587)           # Создаем объект SMTP
server.set_debuglevel(True)                         # Включаем режим отладки - если отчет не нужен, строку можно закомментировать
server.starttls()                                   # Начинаем шифрованный обмен по TLS
server.login(addr_from, password)                   # Получаем доступ
server.send_message(msg)                            # Отправляем сообщение
server.quit()                                       # Выходим
'''



