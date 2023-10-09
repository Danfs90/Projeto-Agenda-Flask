# Importe as classes necessárias
from sqlalchemy import Integer, DateTime, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from projeto_agenda.models.clients import Clients  # Certifique-se de importar corretamente
from projeto_agenda.models.procedures import Procedures  # Certifique-se de importar corretamente
from projeto_agenda.models.base import Base  # Suponho que você tenha uma classe base

class Events(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    client_id = Column(Integer, ForeignKey('clients.id'))
    procedure_id = Column(Integer, ForeignKey('procedures.id'))
    start_event = Column(DateTime)
    end_event = Column(DateTime)

    # Relacionamento com a tabela "Clients"
    client = relationship('Clients', back_populates='events')

    def __init__(self, start_event=None):
        self.start_event = start_event
