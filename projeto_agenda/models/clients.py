from sqlalchemy import Integer,DateTime,VARCHAR,String, Column, ForeignKey
from sqlalchemy.orm import mapped_column,relationship
from projeto_agenda.models.base import Base 


class Clients(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    document = Column(String, nullable=False)
    cellphone = Column(String, nullable=False)
    dt_nasc = Column(DateTime)

    events = relationship('Events', back_populates='client')

    
    def __init__(self, document=None):
        self.document = document    