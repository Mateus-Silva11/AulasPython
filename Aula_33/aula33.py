
#====== biblioteca do Mysql
import MySQLdb
#======= Configurando a conexão
conexao = MySQLdb.connect(host='localhost', database='aula_bd', user='root', passwd='')
#======= Salva o cursor da conexão em uma variavel
cursor= conexao.cursor()
#======= Criação de dicionarario que respresenta uma pessoa

#===== Criaçãoi do comando SQL e passado para o cursor

cursor.execute("SELECT * FROM tb_pessoa")
pessoa = cursor.fetchall()
lista_pesssoa = []
for p in pessoa:
    
    dicionario_pessoa = {'Id_pessoa':0, 'Nome':'', 'SobreNome':'', 'Idade': 0 , 'endereco_id':0}
    dicionario_pessoa['Id_pessoa']= p[0]
    dicionario_pessoa['Nome']= p[1]
    dicionario_pessoa['SobreNome']= p[2]
    dicionario_pessoa['Idade']= p[3]
    dicionario_pessoa['endereco_id']= p[4]
    lista_pesssoa.append(dicionario_pessoa)

with open('Aula_33/pessoa.txt','a') as arquivo:

    for p in lista_pesssoa:
        arquivo.write(f"{p['Id_pessoa']};{p['Nome']};{p['SobreNome']};{p['Idade']};{p['endereco_id']}\n")