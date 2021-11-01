from pydantic import BaseModel
from typing import Optional, List


class User(BaseModel):
    id: Optional[str]=None
    name:str
    telefone:int
    class Config:
        orm_mode=True
   

class Produto(BaseModel):
    id: Optional[str]=None
    nome:str
    preco:float
    detalhes:str
    disponivel:bool=False
    class Config:
        orm_mode=True

class Pedido(BaseModel):
    id: Optional[str]=None
    user: User
    produto:Produto
    quantidade:int
    entrega:bool=True
    endereco: str
    observacoes: Optional[str]="None"
    class Config:
        orm_mode=True