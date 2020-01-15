import MySQLdb
from pessoa import Pessoa
class Pessoa_db: 
    #----- Configurar a conexão
    conexao = MySQLdb.connect(host='localhost', database='aula_bd', user='root', passwd='')
    #----- Salva o cursor da conexão em uma variável
    cursor = conexao.cursor()

    def listar_todos(self):
        #----- Criação do comando SQL e passado para o cursor
        comando_sql_select = "SELECT * FROM tb_pessoa"
        self.cursor.execute(comando_sql_select)
        #---- Pega todos os resultados da execução do comando SQL e armazena em uma variável
        resultado = self.cursor.fetchall()
        lista_pessoas_classe = self.conserter_tabela_classe(resultado)
        return resultado
   
    def bucar_por_id(self):
        self.cursor(f'SELECT * FROM tb_pessoa WHERE Id_pessoa {Id_pessoa}')
        resultado = self.cursor.fetchone()
        return resultado
    
    def converter_tabela_classe(self,lista_tuplas):
    #cria uma lista para armazenar os dicionarios
    lista_pessoas = []
    for p in lista_tuplas:
        #----- Criação do objeto da classe pessoa
        p1 = Pessoa()
        #--- pega cada posição da tupla e atribui a uma chave do dicionário
        p1.Id_pessoa = p[0]
        p1.Nome = p[1]
        p1.SobreNome = p[2]
        p1.Idade = p[3]
        p1.endereco_id = p[4]
        lista_pessoas.append(p1)
    return lista_pessoas
