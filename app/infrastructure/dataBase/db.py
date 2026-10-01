import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
load_dotenv()

engine = create_engine(os.environ["DATABASE_URL"])
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def depends_db():
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()