import MySQLdb

def listar_todos():
    #----- Configurar a conexão
    conexao = MySQLdb.connect(host='localhost', database='aula_bd', user='root', passwd='')
    #----- Salva o cursor da conexão em uma variável
    cursor = conexao.cursor()
    #----- Criação do comando SQL e passado para o cursor
    comando_sql_select = "SELECT * FROM tb_pessoa"
    cursor.execute(comando_sql_select)
    #---- Pega todos os resultados da execução do comando SQL e armazena em uma variável
    resultado = cursor.fetchall()
    return resultado