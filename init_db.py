from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Creating a database and table
DATABASE_URL = 'sqlite:///school_data.db'

engine = create_engine(DATABASE_URL)
Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    age = Column(Integer)
    grade = Column(String)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
