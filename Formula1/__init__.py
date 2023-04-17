from flask import Flask
from flask_mysqldb import MySQL
from logging.config import dictConfig

dictConfig({
  'version': 1,
  'formatters': {
    'user' : {
        'format' :  '%(message)s'
    }
  },
  'handlers': {
    'wsgi': {
      'class': 'logging.StreamHandler',
      'stream': 'ext://flask.logging.wsgi_errors_stream',
      'level' : 'INFO'
    },
    'file': {
      'class': 'logging.FileHandler',
      'filename': 'logs.log',
      'formatter': 'user',
      'level' : 'DEBUG'
    }
  },
  'root': {
    'handlers': ['wsgi','file']
  }
})

app = Flask(__name__)

app.secret_key = 'many random bytes'
app.config['MYSQL_HOST'] = 'formula1-mysql.mysql.database.azure.com'
app.config['MYSQL_USER'] = 'dev'
app.config['MYSQL_PASSWORD'] = 'admin@azure123'
app.config['MYSQL_DB'] = 'Formula1'
mysql = MySQL(app)

app.logger.debug("DATABASE CONFIGURED WITH APP")

