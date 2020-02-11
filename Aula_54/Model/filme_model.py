import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
BaseAlchemy = declarative_base()

class FilmeModel(BaseAlchemy):
    #Confugrando a Tabela para o alchemy entender
    # #Nome da tabela
    __tablename__ = "Filme"
    # coluna da Tabela / comando do alchemy / informando que uma PK = primary_key
    id = db.Column(db.Integer, primary_key=True)
    # coluna da Tabela / comando do alchemy / informando tipo da variavel / definindo tamanho
    Nome= db.Column(db.String(length=45))
    # coluna da Tabela / comando do alchemy / informando tipo da variavel / definindo tamanho
    Descricao = db.Column(db.String(length=45))

    #Metodo para mostra os objetos da class nao muito eficiente neste caso
    def __str__(self):
        return "{}-{}-{}".format(self.id, self.Nome,self.Descricao)