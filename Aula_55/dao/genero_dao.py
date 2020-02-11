from Aula_55.dao.base_dao import BaseDao
from Aula_55.model.genero import Genero

class GeneroDao(BaseDao):
    def __init__(self):
        super().__init__(Genero)
