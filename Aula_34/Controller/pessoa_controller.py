import sys
sys.path.append('C:/Users/900148/Desktop/GitHub/AulasPython/Aula_34')

from Dao.pessoa_dao import PessoaDao
from Model.pessoa import Pessoa

class PessoaConreoller:
    dao = PessoaDao()

    def listar_todos(self):
        return self.dao.listar_todos()

    def buscar_por_id(self):
        return self.dao.buscar_id(Id_pessoa)

    def salvar (self , pessoa : Pessoa):
        return self.dao.salvar(pessoa)

    def alterar (self, pessoa : Pessoa):
        self.dao.alterar(pessoa)

    def deletar(self, Id_pessoa):
        self.dao.deletar(Id_pessoa)


    