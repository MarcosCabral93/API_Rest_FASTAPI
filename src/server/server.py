from fastapi import FastAPI, Depends
from src.infra.sqlalchemy.config.config import criar_bd, get_db
from ..schemas.schemas import Produto, User
from ..infra.sqlalchemy.controllers.produto import RepositorioProduto
from ..infra.sqlalchemy.controllers.user import UserController
from sqlalchemy.orm import Session
app=FastAPI()
criar_bd()
@app.post('/produtos')
def criar_produtos(produto:Produto, db: Session=Depends(get_db)):
    produto_criado=RepositorioProduto(db).criar(produto)
    return produto_criado

@app.get('/produtos')
def listas_produtos(db: Session=Depends(get_db)):
    produtos=RepositorioProduto(db).listar()
    return produtos

@app.get('/users')
#Instancio o Schema e uso depends para encontrar o db
def listar_users( db: Session=Depends(get_db)):
    users=UserController(db).listar()
    return users

@app.post('/users')
def criar_users(user:User, db: Session=Depends(get_db) ):
    user_criado=UserController(db).criar(user)
    return user_criado