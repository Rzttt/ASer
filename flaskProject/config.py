import os
basedir = os.path.abspath(os.path.dirname(__file__))

class ASer_db(object):
    SECRET_KEY = '20011117rt'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/ASer'
    SQLALCHEMY_TRACK_MODIFICATIONS = False