import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'l5Fxa42kxK3q'

DATABASE_PATH = os.path.join(basedir, DATABASE)

SQALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH