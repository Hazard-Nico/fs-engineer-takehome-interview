import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    HOST = str(os.environ.get("DB_HOST"))
    DATABASE = str(os.environ.get("DB_DATABASE"))
    USERNAME = str(os.environ.get("DB_USERNAME"))
    PASSWORD = str(os.environ.get("DB_PASSWORD"))
    
    JWT_SECRET_KEY = str(os.environ.get("JWT_SECRET"))
    
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + USERNAME + '@' + HOST + '/' + DATABASE + '?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLACHEMY_RECORD_QUERIES = True

    UPLOAD_FOLDER = str(os.environ.get("UPLOAD_FOLDER"))