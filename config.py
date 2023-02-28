import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    username = os.environ.get('DATABASE_USERNAME')
    password = os.environ.get('DATABASE_PASSWORD')
    database_name = os.environ.get('DATABASE_NAME')

    SQLALCHEMY_DATABASE_URI = 'mysql://{0}:{1}@localhost/{2}'.format(username, password, database_name)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass
