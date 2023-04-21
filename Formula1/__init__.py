from flask import Flask
from logging.config import dictConfig
import sqlite3
import os

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


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "Formula1.db")
conn = sqlite3.connect(db_path, check_same_thread=False)



