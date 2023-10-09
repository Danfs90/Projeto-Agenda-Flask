from sqlalchemy.orm import sessionmaker
from sqlalchemy import  create_engine
from projeto_agenda.models.base import Base

engine = create_engine('sqlite:///database.db')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

