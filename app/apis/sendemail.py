from flask_mail import Message
from flask_restful import Resource
from app.plugin import mail


class SendEmailTest(Resource):
    def get(self):
        msgData = {
             'subject':'SendEmailTest',
             'recipients':['miyukinakajima1994@gmail.com','tianxing1994@hotmail.com'],
             'body':'SendEmailTest',
             'html':None,
             'sender':'1003593179@qq.com',  # 发件人，必须与初始化 mail 对象时的 MAIL_USERNAME 一样
             'cc':['miyukinakajima1993@gmail.com',],    # 抄送
             'bcc':['miyukinakajima1995@gmail.com',],   # 密送
             'attachments':None,    # 还不会添加附件
             'reply_to':None,
             'date':None,
             'charset':None,
             'extra_headers':None,
             'mail_options':None,
             'rcpt_options':None,
        }
        msg = Message(**msgData)
        mail.send(msg)
        result = {'message':'Success!'}
        return result