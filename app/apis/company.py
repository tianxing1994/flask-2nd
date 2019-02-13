import time
from flask_restful import Resource, marshal_with, fields, marshal
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
        data = {
            'status': 200,  # 状态码
            'time': time.time(),  # 请求时间
            'message': "Success!",  # 提示信息
            'company': company,
            'users':users
        }
        return data



class Allcompany(Resource):
    def get(self):
        # user 数据格式化
        users_fields = {
            'id':fields.Integer,
            'username':fields.String,
            'password':fields.String,
            'age':fields.Integer,
            'sex':fields.Boolean,
            'job':fields.String,
        }

        # recource 数据格式化
        resource_fields = {}

        # 所有公司对象，数据类型 List
        companys = models.Company.query.all()
        # 响应结果对象，Python 字典
        result = {}

        for company in companys:
            # 根据公司的实际数量生成 resource 数据格式化字典
            resource_fields.update({company.companyName:fields.List(fields.Nested(users_fields))})
            # 生成 result 字典对象
            data = {company.companyName:company.users}
            result.update(data)
        return marshal(result,resource_fields)