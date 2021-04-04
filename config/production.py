from logging.config import dictConfig
from config.default import *


# SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user='dbmasteruser',
    pw=':cb=8*6[M**eAcw.aB84_8Na~&eENm3+',
    url='ls-26a5903283b670e9a69c4ec02c3178f89d7d0419.cw82n8y66zer.ap-northeast-2.rds.amazonaws.com',
    db='flask_pybo'
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'{\xdb\xe4`jL&\xb1`i\xf4\xeaP\xdde\x15'

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/myproject.log'),
            'maxBytes': 1024 * 1024 * 5, # 5MB
            'backupCount': 5,
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    }
})