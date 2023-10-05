from sqlalchemy.orm import DeclarativeBase,Mapped
from sqlalchemy import Integer,DateTime,VARCHAR,String, Column
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class Events(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    start_event = Column(DateTime)
    end_event = Column(DateTime)
    
    def __init__(self, start_event=None):
        self.start_event = start_event    