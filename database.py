from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os, sys
basedir = os.path.abspath(os.path.dirname(__file__))


SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
print("------------------------------")
print("------------------------------")
print("------------------------------")
print(SQLALCHEMY_DATABASE_URL)
print("------------------------------")
print("------------------------------")
print("-----------------------------")
sys.stdout.flush()
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()