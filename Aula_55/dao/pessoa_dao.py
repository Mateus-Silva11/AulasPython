from Aula_55.dao.base_dao import BaseDao
from Aula_55.model.pessoa import Pessoa

class PessoaDao(BaseDao):
    def __init__(self):
        super().__init__(Pessoa)
