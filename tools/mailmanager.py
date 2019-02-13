from flask import render_template
from flask_mail import Message


def send_email_active_link(email,active_link,mail):
    context = {'email':email,'active_link':active_link}
    html = render_template('email/active.html', **context)

    message = {
        'subject': 'User mailbox verification',
        'recipients': [email, 'miyukinakajima1994@gmail.com'],
        'body': None,
        'html': html,
        'sender': '1003593179@qq.com',  # 发件人，必须与初始化 mail 对象时的 MAIL_USERNAME 一样
        'cc': ['miyukinakajima1993@gmail.com', ],  # 抄送
        'bcc': ['miyukinakajima1995@gmail.com', ],  # 密送
        'attachments': None,  # 还不会添加附件
        'reply_to': None,
        'date': None,
        'charset': None,
        'extra_headers': None,
        'mail_options': None,
        'rcpt_options': None,
    }
    msg = Message(**message)
    mail.send(msg)
    result = True
    return result