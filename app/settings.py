import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 's29o)40!yp=-3*ods9v^4*6=&vrrz_*!-efjz6jrsisqkssx25'

SESSION_TYPE = 'redis'

DEBUG = True
TESTING = False
# DEBUG_TB_INTERCEPT_REDIRECTS = False
# DEBUG_TB_ENABLED = True
# DEBUG_TB_HOSTS = [*]
# DEBUG_TB_PANELS = False
# DEBUG_TB_PROFILER_ENABLED = True
# DEBUG_TB_TEMPLATE_EDITOR_ENABLED = True

DATABASES = {
    'mysql': {
        # dialect+driver://username:password@host:port/database
        'DIALECT': 'mysql',
        'DRIVER':'pymysql',
        'USERNAME': 'root',
        'PASSWORD': 'rock1204',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME':'flasktest',
    },

    'sqlite': {
        # 'sqlite:///flaskTest.db'
        'NAME': os.path.join(BASE_DIR,'flaskTest.db'),
    },
}


CACHE = {
    'ENABLE' : 'redis',
    'redis' : {
        'CACHE_TYPE': 'redis',
        'CACHE_KEY_PREFIX': 'python(Flask)',
    },
    'simple' : {
        'CACHE_TYPE': 'simple',
    },
}


EMAIL = {
    'ENABLE': 'qq',
    '163' : {
        'MAIL_SERVER' : 'smtp.163.com',
        'MAIL_PORT' : 25,
        'MAIL_USE_TLS' : False,
        'MAIL_USE_SSL' : False,
        'MAIL_USERNAME' : 'tianxingfacebook@163.com',
        'MAIL_PASSWORD' : 'tian201128010420',
        'MAIL_DEFAULT_SENDER' : None,
        'MAIL_MAX_EMAILS' : None,
        'MAIL_ASCII_ATTACHMENTS' : False,
    },

    'qq' : {
        'MAIL_SERVER': 'smtp.qq.com',
        'MAIL_PORT': 25,
        'MAIL_USE_TLS': False,
        'MAIL_USE_SSL': False,
        'MAIL_USERNAME': '1003593179@qq.com',
        'MAIL_PASSWORD': 'lnholfgulflxbfae',    # 需要使用专用授权码
        'MAIL_DEFAULT_SENDER': None,
        'MAIL_MAX_EMAILS': None,
        'MAIL_ASCII_ATTACHMENTS': False,
    }
}