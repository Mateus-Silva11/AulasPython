from Aula_55.dao.base_dao import BaseDao
from Aula_55.model.editora import Editora

class EditoraDao(BaseDao):
    def __init__(self):
        super().__init__(Editora)
