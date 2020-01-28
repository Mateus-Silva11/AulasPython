import sys
sys.path.append(r'C:\Users\900148\Desktop\GitHub\AulasPython\Aula_37')
from Dao.squad_dao import SquadDao
from Model.squad import Squad

class SquadController:
    dao = SquadDao()

    def listar_todos(self):
        lista_squad = []
        lista_tuplas = self.dao.listar_todos()
        for s in lista_tuplas:
            squad = Squad()
            squad.idSquad =  s[0]
            squad.Nome = s[1]
            squad.Descricao = s[2]
            squad.NumeroPessoas = s[3]
            squad.LinguagemBackEnd = s[4]
            squad.FrameworkFrontEnd = s[5]
            lista_squad.append(squad)
        print(lista_squad)
        for i in lista_squad:
            print(i) 
        return lista_squad

    def buscar_por_id(self, idSquad):
        s = self.dao.buscar_por_id(idSquad)
        squad = Squad()
        squad.idSquad =  s[0]
        squad.Nome = s[1]
        squad.Descricao = s[2]
        squad.NumeroPessoas = s[3]
        squad.LinguagemBackEnd = s[4]
        squad.FrameworkFrontEnd = s[5]
        return squad

    def salvar(self, suqad:Squad):
        return self.dao.salvar(squad)

    def alterar(self, squad:Squad):
        self.dao.alterar(pessoa)

    def deletar(self, idSquad):
        self.dao.deletar(idSquad)

if __name__ == "__main__":
    a=SquadController()
    a.listar_todos()