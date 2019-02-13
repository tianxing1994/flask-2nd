import random
import time

from flask import request
from flask_restful import Resource, marshal_with, fields, marshal,reqparse
from app import models
from tools import encrypt,mailmanager
from app.plugin import cache
from app.plugin import mail

class SignUp(Resource):
    # 创建用户
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, help='username error')
        parser.add_argument('password', type=str, help='password error')
        parser.add_argument('email', type=str, help='email error')
        parser.add_argument('phone', type=str, help='phone error')
        args = parser.parse_args()

        ip = request.remote_addr
        timestamp = time.time()
        random_num = random.randrange(1000,9999)
        real_token = str(ip) + str(timestamp) + str(random_num)
        token = encrypt.encrypt_md5(real_token)

        member = models.Members(
            username=args.get('username'),
            password=args.get('password'),
            email=args.get('email'),
            phone=args.get('phone'),
            token=token
        )

        result = {
            'time': time.time(),  # 请求时间
        }

        try:
            models.db.session.add(member)
            models.db.session.commit()
            cache.set(token, True, timeout=30 * 60)
            result['status'] = 200
            result['message'] = 'Success!'

            active_link = r'10.20.152.50:8000/api/v1/signup/?token={}'.format(token)
            result['active_link'] = active_link

            mailmanager.send_email_active_link(member.email,active_link,mail)
            result['sent_email'] = True
            result['success'] = True
        except Exception as e:
            result['status'] = 422
            result['success'] = False
            result['message'] = 'Failed!'

        return result
    # 激活用户
    def get(self):
        result = {
            'status': '',  # 状态码
            'time': time.time(),  # 请求时间
            'message': '',  # 提示信息
        }
        token = request.args.get('token')
        if cache.get(token):
            the_member = models.Members.query.filter(models.Members.token==token).first()
            the_member.is_active = True
            models.db.session.add(the_member)
            models.db.session.commit()
            result['status'] = 200
            result['success'] = True
            result['message'] = 'Successfully active the member!'
        else:
            result['status'] = 401
            result['success'] = False
            result['message'] = 'Token expired or not exist!'
        return result

class SignIn(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, help='username error')
        parser.add_argument('password', type=str, help='password error')
        args = parser.parse_args()
        print(args)

        username = args.get('username')
        password = args.get('password')

        the_member = models.Members.query.filter(models.Members.username==username,models.Members.password==password).first()
        result = {
            'time': time.time(),  # 请求时间
        }

        if the_member and not the_member.is_delete and the_member.is_active:
            print('用户存在，未删除，激活状态')
            result['status'] = 200
            result['success'] = True
            result['message'] = 'Success!'
        elif the_member and not the_member.is_delete and not the_member.is_active:
            print('用户存在，未删除，未激活')
            result['status'] = 406
            result['success'] = False
            result['message'] = 'Did not active email!'
        else:
            print('用户不可用')
            result['status'] = 402
            result['success'] = False
            result['message'] = 'User or password error'
        return result



