import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 's29o)40!yp=-3*ods9v^4*6=&vrrz_*!-efjz6jrsisqkssx25'

SESSION_TYPE = 'redis'

DEBUG = True
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
