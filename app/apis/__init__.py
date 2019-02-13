from app.plugin import api
from . import apitest,company,sendemail,signin


api.add_resource(apitest.HelloWorld, '/api/v1/helloworld/')
api.add_resource(company.Company, '/api/v1/company/<int:id>/')
api.add_resource(company.Allcompany, '/api/v1/allcompany/')
api.add_resource(sendemail.SendEmailTest, '/api/v1/sendemailtest/')
api.add_resource(signin.SignUp, '/api/v1/signup/')
api.add_resource(signin.SignIn, '/api/v1/signin/')



