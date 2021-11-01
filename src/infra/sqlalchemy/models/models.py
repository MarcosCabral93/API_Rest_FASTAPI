from sqlalchemy import Column, Integer,String,Float,Boolean
from ..config.config import Base

class Produto(Base):
    __tablename__ ="produto"

    id=Column(Integer, primary_key=True, index=True)
    nome =Column(String)
    detalhes=Column(String)
    preco=Column(String)
    preco =Column(Float)
    disponivel=Column(Boolean)

class User(Base):
    __tablename__ ="user"

    id=Column(Integer,primary_key=True, index=True )
    name=Column(String)
    telefone=Column(Integer, )