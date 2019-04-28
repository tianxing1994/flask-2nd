from flask import Blueprint
from flask import Flask
from flask_script import Manager

blue = Blueprint('first', __name__)
app = Flask(__name__)
app.register_blueprint(blueprint=blue)
manager = Manager(app)


@blue.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    manager.run()

# 在 Tetmimal 命令行执行 python mymanage.py runserver 以启运服务