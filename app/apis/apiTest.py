from flask_restful import Resource

class HelloWorld(Resource):
    def post(self):
        return {'POST':'Hello World'}

    def get(self):
        return {'GET':'Hello World'}

