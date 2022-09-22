import os
from dotenv import load_dotenv

# Get the file path to our .env file
basedir = os.path.abspath(os.path.dirname(__name__))

# Take the basedir, and use it to load in your .env file
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    FLASK_DEBUG = os.getenv('FLASK_DEBUG')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')