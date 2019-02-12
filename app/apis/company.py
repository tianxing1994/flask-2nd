import time
from flask_restful import Resource, marshal_with, fields
from app import models


company_fields = {
    'id' : fields.Integer,
    'companyName' : fields.String,
    'companyType' : fields.String,
}

users_fields = {
    'id':fields.Integer,
    'username':fields.String,
    'password':fields.String,
    'age':fields.Integer,
    'sex':fields.Boolean,
    'job':fields.String,
}

resource_fields = {
    'status': fields.Integer,  # 状态码
    'time': fields.Float,  # 请求时间
    'message': fields.String,  # 提示信息
    'company': fields.Nested(company_fields),
    'users': fields.List(fields.Nested(users_fields)),
}

class Company(Resource):
    @marshal_with(resource_fields)
    def get(self,id):
        # company = models.Company.query.get(id)
        company = models.Company.query.filter(models.Company.id == id).first()
        users = company.users
        print(users)
        data = {
            'status': 200,  # 状态码
            'time': time.time(),  # 请求时间
            'message': "Success!",  # 提示信息
            'company': company,
            'users':users
        }
        return data