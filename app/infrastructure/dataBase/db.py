import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
load_dotenv()

from sqlalchemy.orm import sessionmaker, declarative_base
engine = create_engine(os.environ["DATABASE_URL"])
sessionLocal = sessionmaker(bind=engine)
Base = declarative_base()