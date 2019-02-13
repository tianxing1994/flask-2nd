from flask_caching import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_restful import Api
from flask_mail import Mail, string_types
from . import settings


db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()
toolbar = DebugToolbarExtension()
cache = Cache()
api = Api()
mail = Mail()

def plugin_init(app):

    # 配置调试状态
    app.config['DEBUG'] = settings.DEBUG # 或： app.debug = True

    # 配置 session
    app.config['SECRET_KEY'] = settings.SECRET_KEY
    app.config['SESSION_TYPE'] = settings.SESSION_TYPE
    Session(app)

    # 配置数据库
    # dialect+driver://username:password@host:port/database
    # SQLALCHEMY_DATEBASE_URI = 'mysql+pymysql://root:rock1204@127.0.0.1:3306/flasktest'
    DATABASE = settings.DATABASES.get('mysql')

    SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}'.format(
        DATABASE.get('DIALECT'),
        DATABASE.get('DRIVER'),
        DATABASE.get('USERNAME'),
        DATABASE.get('PASSWORD'),
        DATABASE.get('HOST'),
        DATABASE.get('PORT'),
        DATABASE.get('NAME'),
    )

    # 'sqlite:///flaskTest.db'
    # DATABASE = settings.DATABASES.get('sqlite')
    # SQLALCHEMY_DATABASE_URI = 'sqlite:////' + DATABASE.get('NAME'),


    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    # 配置 Migrate
    migrate.init_app(app=app,db=db)

    # 配置 Bootstrap
    bootstrap.init_app(app)

    # 配置 DebugToolbar
    toolbar.init_app(app)

    # 配置缓存
    # cache = Cache(config={'CACHE_TYPE': 'simple'})
    # cache.config = {
    #     'CACHE_TYPE': 'redis',
    #     'CACHE_KEY_PREFIX': 'python(Flask)'
    # }

    cache.config = settings.CACHE.get(settings.CACHE.get('ENABLE'))
    cache.init_app(app)

    # 配置 Api
    api.init_app(app)

    # 配置 mail
    mail_config = settings.EMAIL.get(settings.EMAIL.get('ENABLE'))
    app.config.from_mapping(mail_config)
    mail.init_app(app)
