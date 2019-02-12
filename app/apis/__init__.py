from app.plugin import api
from . import apiTest,company


api.add_resource(apiTest.HelloWorld, '/api/v1/helloworld/')
api.add_resource(company.Company, '/api/v1/company/<int:id>/')


