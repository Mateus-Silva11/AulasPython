import sqlalchemy as db
# criando a class base_dao Orientação a objeto simplificando o codigo
class BaseDao:
    def __init__(self):
        #criando a conexeção com o banco de dados
        # ----database+conector://user:passwd@url:porta/database
        conexao = db.create_engine("mysql+mysqlconnector://topskills01:ts2019@mysql.topskills.dev:3306/topskills01")
        #criando uma sessao
        criador_sessao = db.orm.sessionmaker()
        criador_sessao.configure(bind=conexao)
        self.sessao = criador_sessao()
