from sqlalchemy import Integer,DateTime,VARCHAR,String, Column, ForeignKey
from sqlalchemy.orm import mapped_column,relationship
from projeto_agenda.models.base import Base  


class Procedures(Base):
    __tablename__ = 'procedures'

    id = Column(Integer, primary_key=True)
    name_procedures = Column(String, nullable=False)
    time = Column(String, nullable=False)



    def __init__(self, name_procedures=None):
        self.name_procedures = name_procedures    
