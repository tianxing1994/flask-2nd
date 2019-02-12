from flask import Flask
from . import views


def createapp():
    app = Flask(__name__)

    # 配置插件
    views.blue_init(app)

    return app



