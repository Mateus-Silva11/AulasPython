import MySQLdb

#Listando Todos dados da tabela
def listar_todos(c):
    c.execute('SELECT * FROM tb_pessoa')
    pessoas = c.fetchall()
    for p  in  pessoas:
        print(p)

#Buscar pelo id
def buscar_por_id(c, id):
    c.execute(f'SELECT * FROM tb_pessoa WHERE ID = {id}')
    pessoa = c.fetchone()
    print(pessoa)

#Buscar por Sobrenome
def buscar_por_sobrenome(c, sobrenome):
    c.execute(f"SELECT * FROM tb_pessoa WHERE SOBRENOME like '{sobrenome}%' ")
    for p  in  c.fetchall():
        print(p)


#Salvar Pessoa
def salvar(cn,cr,Nome,SobreNome,Idade, endereco_id='NULL'):
    cr.execute(f"INSERT INTO tb_pessoa (Nome,SobreNome,Idade,endereco_id) VALUES ('{Nome}', '{SobreNome}' , {Idade} , {endereco_id} ) ")
    cn.commit()

#Alterar Pessoa
def alterar(cn,cr,Id_pessoa,Nome,SobreNome,Idade, endereco_id='NULL'):
    cr.execute(f"UPDATE tb_pessoa SET Nome='{Nome}', Sobrenome='{SobreNome}' , Idade={Idade} , endereco_id={endereco_id}  WHERE Id_pessoa={Id_pessoa}")
    cn.commit()

#Deletar Pessoa
def deletar(cn, cr, Id_pessoa):
    cr.execute(f'DELETE FROM tb_pessoa WHERE Id_pessoa={Id_pessoa}')
    cn.commit()

conexao = MySQLdb.connect(host='localhost', database='aula_bd', user='root', passwd='')
cursor= conexao.cursor()

#Comandos Para CRUD  Pessoa;

# listar_todos(cursor)
# buscar_por_id(cursor, 2)
# buscar_por_sobrenome(cursor,'Sil')
# salvar(conexao,cursor,'Pablo','Cardoso',12,2)
# alterar(conexao,cursor, 3 ,'Rafaela','Mendes',18, 1)
# deletar(conexao,cursor,3)




#Listando Todos dados da tabela

#Lista todos os dados do endereço
def listar_todos_endereco(cr):
    cr.execute('SELECT * FROM tb_endereco')
    #Pega todos as linha do resultado SELECT
    endereco = cr.fetchall()
    for e  in  endereco:
        print(e)

#Buscar pelo id_endeco

def buscar_por_id_endereco(cr, Id_endereco):
    cr.execute(f'SELECT * FROM tb_endereco WHERE Id_endereco = {Id_endereco}')
    endereco = cr.fetchone()
    print(endereco)

#Buscar por Dado

def buscar_por_cep(cr, cep):
    cr.execute(f"SELECT * FROM tb_endereco WHERE cep like {cep} ")
    for c  in  cr.fetchall():
        print(c)

def salvar_endereco(cr,cn,Id_endereco,Rua,cep,bairro):
    cr.execute(f"INSERT INTO tb_endereco (Id_endereco,Rua,cep,bairro)VALUES ({Id_endereco}, '{Rua}', '{cep}' , '{bairro}' )")
    cn.commit()

def alterar_endereco(cr,cn,Id_endereco,Rua,cep,bairro):
    cr.execute(f"UPDATE tb_endereco SET Id_endereco={Id_endereco} , Rua='{Rua}' , cep='{cep}' , bairro='{bairro}' where Id_endereco={Id_endereco} ")
    cn.commit()


#CRUD Endereço

#listar_todos_endereco(cursor)
#buscar_por_id_endereco(cursor,2)
#buscar_por_cep(cursor,231321 )
#salvar_endereco(cursor,conexao,3,'Rua Santa Maria','23432','Progresso')
alterar_endereco(cursor,conexao,2,'Rua Rui Barbosa','324435','Progresso')