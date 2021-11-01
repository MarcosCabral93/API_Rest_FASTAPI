from sqlalchemy.orm import Session
from ....schemas import schemas
from ..models import models
class RepositorioProduto():
    def __init__(self, db:Session):
        self.db=db

    def criar (self, produto:schemas.Produto):
        db_produto=models.Produto(nome=produto.nome,
        detalhes=produto.detalhes, preco=produto.preco, disponivel=produto.disponivel)
        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return db_produto
    
    def listar(self):
        produtos=self.db.query(models.Produto).all()
        return produtos