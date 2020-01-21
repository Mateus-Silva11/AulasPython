import MySQLdb
from 2-Model.endereco import Endereco 

class EnderecoDao:
    conexao = MySQLdb.connect(host='localhost',database='aula_bd',user='root',passwd='' )
    cursor = conexao.cursor()

    def listar_tados(self):
        comando = f" SELECT * FROM tb_endereco"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado

    def buscar_id(self,Id_endereco):
        pass

    def salvar(self, endereco:Endereco ):
        pass

    def alterar(self, endereco:Endereco):
        pass

    def deletar(self, Id_endereco):
        pass