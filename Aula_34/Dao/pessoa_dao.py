import MySQLdb
from Model.pessoa import Pessoa 

class PessoaDao:
    conexao = MySQLdb.connect(host='localhost',database='aula_bd',user='root',passwd='' )
    cursor = conexao.cursor()

    def listar_tados(self):
        comando = f" SELECT * FROM tb_pessoa"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado

    def buscar_id(self,Id_pessoa):
        comando = f"SELECT * FROM tb_pessoa where Id_pessoa={Id_pessoa}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
        
    def salvar(self, pessoa:Pessoa ):
        comando = f''' 
        INSERT INTO tb_pessoa (
        Id_pessoa,Nome,SobreNome,Idade,enderco_id
        )
        VALUES(
            {pessoa.Id_pessoa};
            '{pesssoa.Nome}';
            '{pesssoa.SobreNome}';
            {pessoa.Idade};
            {pessoa.enderco_id}
        )        
        '''
        self.cursor.execute(comando)
        self.conexao.commit()

    def alterar(self, pessoa:Pessoa):
        comando = f'''
        UPDATE tb_pessoa set Nome = {pessoa.Nome}, SobreNome = {pessoa.SobreNome}; Idade = {pessoa.Idade} ; endereco_id = {pessoa.endereco_id}
        where Id_pessoa = {pessoa.Id_pessoa}
        '''
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, Id_pessoa):
        comando = f'DELETE FROM Id_endereco WHERE Id_endereco={Id_endereco}'
        self.cursor.execute(comando)
        self.conexao.commit()
