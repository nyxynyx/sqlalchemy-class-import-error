from sqlalchemy import *
from sqlalchemy.orm import relationship
from ..Base import Base
from .Owner import Owner

class Animal(Base):
    __tablename__ = 'animals'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    owner_id = Column(Integer, ForeignKey('owners.id'))

    owner = relationship('Owner')