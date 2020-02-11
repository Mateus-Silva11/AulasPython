from Aula_55.dao.base_dao import BaseDao
from Aula_55.model.autor import Autor

class AutorDao(BaseDao):
    def __init__(self):
        super().__init__(Autor)