from datetime import timedelta
from flask_caching import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_restful import Api
from flask_mail import Mail
from app import settings

db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()
toolbar = DebugToolbarExtension()
cache = Cache()
api = Api()
# mail = Mail()

def plugin_init(app):

    # 配置调试状态
    app.config['DEBUG'] = settings.DEBUG # 或： app.debug = True

    # 配置密钥
    app.config['SECRET_KEY'] = settings.SECRET_KEY

    # 配置 session
    session_config = settings.SESSION.get(settings.SESSION.get('ENABLE'))
    app.config.from_mapping(session_config)
    Session(app)

    # 配置数据库
    # MySQL数据库：
    # dialect+driver://username:password@host:port/database
    # SQLALCHEMY_DATEBASE_URI = 'mysql+pymysql://root:rock1204@127.0.0.1:3306/flasktest'
    # Sqlite数据库：
    # sqlite://// 三个杠代表相对路径，四个杠代表纯对路径
    # sqlite:////path + filename
    # 'sqlite:///flaskTest.db'
    # DATABASE = settings.DATABASES.get('sqlite')
    # SQLALCHEMY_DATABASE_URI = 'sqlite:////' + DATABASE.get('NAME'),
    DATABASE = settings.DATABASES.get(settings.DATABASES.get('ENABLE'))
    DIALECT = DATABASE.get('DIALECT')
    if DIALECT == 'mysql':
        SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}'.format(
            DIALECT,
            DATABASE.get('DRIVER'),
            DATABASE.get('USERNAME'),
            DATABASE.get('PASSWORD'),
            DATABASE.get('HOST'),
            DATABASE.get('PORT'),
            DATABASE.get('NAME'),
        )
    elif DIALECT == 'sqlite':
        SQLALCHEMY_DATABASE_URI = '{}:////{}'.format(
            DIALECT,
            DATABASE.get('NAME'),
        )
    else:
        SQLALCHEMY_DATABASE_URI = ''

    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # 配置 Migrate
    migrate.init_app(app=app,db=db)

    # 配置 Bootstrap
    bootstrap.init_app(app)

    # 配置 DebugToolbar
    app.config.from_mapping = settings.DEBUG_TOOL_BAR
    toolbar.init_app(app)

    # 配置缓存
    cache.config = settings.CACHE.get(settings.CACHE.get('ENABLE'))
    cache.init_app(app)

    # 配置 Api
    api.init_app(app)

    # 配置 mail
    # mail_config = settings.EMAIL.get(settings.EMAIL.get('ENABLE'))
    # app.config.from_mapping(mail_config)
    # mail.init_app(app)



if __name__ == '__main__':
    mail_config = settings.EMAIL.get(settings.EMAIL.get('ENABLE'))
    print(mail_config)

    from flask import Flask

    mail = Mail()

    app = Flask(__name__)
    app.config.from_mapping(mail_config)
    mail.init_app(app)
