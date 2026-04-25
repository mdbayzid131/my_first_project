from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# এই তিনটা লাইন SQLAlchemy লাইব্রেরি থেকে ৩টা জিনিস আনছে:

# create_engine → ডেটাবেসের সাথে সংযোগ তৈরি করে
# declarative_base → টেবিল বানানোর "বেস ক্লাস" তৈরি করে
# sessionmaker → ডেটাবেসের সাথে কাজ করার সেশন বানায়

SQLALCHEMY_DATABASE_URL='postgresql://postgres:1234@localhost/my first project'
engine=create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)




def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

        