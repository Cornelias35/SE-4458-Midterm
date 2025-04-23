from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "postgresql://bedirhan:oPs2iH6kOIEoJMsFEi3fyPDYiDGYY7La@dpg-d04hbrbuibrs73b3kne0-a.oregon-postgres.render.com/backend_midterm"

Base = declarative_base()

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)