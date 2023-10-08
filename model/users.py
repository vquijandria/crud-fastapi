from sqlalchemy import Column, Integer, String
from config.db import Base, engine

class User(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String(20))
    nombre = Column(String(200))
    rol = Column(String(200))
    estado = Column(Integer)

Base.metadata.create_all(bind=engine)
