from sqlalchemy.orm import sessionmaker
from sqlalchemy import  create_engine


engine = create_engine('sqlite:///database.db')

Session = sessionmaker(bind=engine)
session = Session()