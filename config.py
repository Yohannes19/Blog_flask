import os
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists ,create_database


#basedir=os.path.abspath(os.path.dirname(__file__))

if not os.getenv("DATABASE_URL",default="true"):
    raise RuntimeError("DATABASE_URL is not set")

engine= create_engine(os.getenv("DATABASE_URI"))

if not database_exists(engine.url):
    create_database(engine.url)
print(database_exists(engine.url))   

class Config:
    #SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    
    