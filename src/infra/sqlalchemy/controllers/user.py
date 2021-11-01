from sqlalchemy.orm import Session
from ....schemas import schemas
from ..models import models

class UserController():
    def __init__(self, db: Session):
        self.db=db
        #recebe schemas==json como argumento
    def criar (self, user:schemas.User):
        #preparando o dado para o BD
        db_user= models.User(name=user.name, telefone=user.telefone)
        # add e commit da alteracao no bd
        self.db.add(db_user)
        self.db.commit()
        #atualizar a instancia com o id que é gerado aleatorio
        self.db.refresh(db_user)
        return db_user


   
    
    def listar(self):
        #query do SQLALCHEMY para traer todos os dados 
        db_user=self.db.query(models.User).all()
        return db_user