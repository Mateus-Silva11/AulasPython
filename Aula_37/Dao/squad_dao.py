import MySQLdb
import sys
sys.path.append(r'C:\Users\900148\Desktop\GitHub\AulasPython\Aula_37')

from Model.squad import Squad

class SquadDao:
    #----- Configurar a conexão
    conexao = MySQLdb.connect(host='localhost', database='atividade', user='root', passwd='')
    #----- Salva o cursor da conexão em uma variável
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"SELECT * FROM Squad"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, idSquad):
        comando = f"SELECT * FROM Squad where IdSquad = {idSquad}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, squad:Squad):
        comando = f""" INSERT INTO Squad
        (
            Nome,
            Descricao,
            NumeroPessoas,
            LinguagemBackEnd,
            FrameworkFrontEnd   
        )
        VALUES
        (
            '{squad.Nome}',
            '{squad.Descricao}',
            {squad.NumeroPessoas},
            '{squad.LinguagemBackEnd}',
            '{squad.FrameworkFrontEnd}'

        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, squad:Squad):
        comando = f""" UPDATE Squad
        SET
            Nome = '{squad.Nome}',
            Descricao ='{squad.Descricao}',
            NumeroPessoas = {squad.NumeroPessoas},
            LinguagemBackEnd= '{squad.LinguagemBackEnd}',
            FrameworkFrontEnd = '{squad.FrameworkFrontEnd}'
        WHERE idSquad = {squad.idSquad}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, idSquad):
        comando = f"DELETE FROM Squad WHERE idSquad = {idSquad}"
        self.cursor.execute(comando)
        self.conexao.commit()
