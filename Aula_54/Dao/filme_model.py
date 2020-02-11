from Aula_54.Dao.base_dao import BaseDao
from Aula_54.Model.filme_model import FilmeModel

class FilmeDao(BaseDao):
    def list_all(self):
        return self.sessao.query(FilmeModel).all()
    def get_by_id(self,id):
        pass
    def get(self):
        pass