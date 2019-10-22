from sqlalchemy import *
from sqlalchemy.orm import relationship
from ..Base import Base

class Owner(Base):
    __tablename__ = 'owners'
    id = Column(Integer, primary_key=True)
    name = Column(Text)