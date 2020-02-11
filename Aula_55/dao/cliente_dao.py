from Aula_55.dao.base_dao import BaseDao
from Aula_55.model.cliente import Cliente

class ClienteDao(BaseDao):
    def __init__(self):
        super().__init__(Cliente)