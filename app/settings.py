import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = 's29o)40!yp=-3*ods9v^4*6=&vrrz_*!-efjz6jrsisqkssx25'


DEBUG = True


TESTING = False


SESSION = {
    'ENABLE' : 'redis',
    'redis' : {
        # PERMANENT_SESSION_LIFETIME： 如果用户在指定时间内未再次访问本网站，则 session 会失效。如再次访问，则重新开始记时。 需要 session.permanent = True（True 为默认值）
        'SESSION_TYPE': 'redis',
        'SESSION_KEY_PREFIX':'session_login_flask',
        'SESSION_COOKIE_NAME':'sessionid',
        'PERMANENT_SESSION_LIFETIME': 2000,
    },
}


DATABASES = {
    'ENABLE' : 'mysql',
    'mysql': {
        # dialect+driver://username:password@host:port/database
        # 'DRIVER'： pymysql-python模块，用于在 python 中操作 MySql 数据库。即纯 Python MySQL 客户端。
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
        # 'DIALECT': dialect 方言，因为不同的数据库为了提高性能，都提供了一些额外的标准或语法，因此对不同的数据库都要指定 dialect 方言。
        # 'NAME'： sqlite 数据库是文件类型，这里需要指定要使用的 sqlite 数据库的路径与文件名。
        'DIALECT': 'sqlite',
        'NAME': os.path.join(BASE_DIR,'flaskTest.db'),
    },
}


DEBUG_TOOL_BAR = {
    'DEBUG_TB_INTERCEPT_REDIRECTS': False,
}


CACHE = {
    'ENABLE' : 'redis',
    'redis' : {
        'CACHE_TYPE': 'redis',
        'CACHE_KEY_PREFIX': 'cache_flask',
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