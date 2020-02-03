import MySQLdb
from Aula_41.Model.endereco_model import EnderecoModel
class EnderecoDao:
    def __init__(self):
        self.connection = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01',passwd='ts2019')
        self.cursor = self.connection.cursor()
        self.lista_c = ['id', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'cep']

    def list_all(self):
        self.cursor.execute("SELECT * FROM 01_MDG_ENDERECO")
        endereco = self.cursor.fetchall()
        print(endereco)

        lista_endereco = []
        for e in endereco:
            dic = dict(zip(self.lista_c,e))
            endereco = EnderecoModel(**dic)
            lista_endereco.append(endereco.__dict__)
        return lista_endereco

    def get_by_id(self, id):
        self.cursor.execute("SELECT * FROM 01_MDG_ENDERECO WHERE ID = {}".format(id))
        e = self.cursor.fetchone()
        dic = dict(zip(self.lista_c, e))
        endereco = EnderecoModel(**dic)

        return  endereco.__dict__

    def insert(self, endereco:EnderecoModel):
        self.cursor.execute("INSERT INTO 01_MDG_ENDERECO (logradouro,numero,complemento,bairro,cidade,cep) VALUES ('{}','{}','{}','{}','{}','{}')".format(endereco.logradouro,endereco.numero,endereco.complemento,endereco.bairro, endereco.cidade, endereco.cep))
        self.connection.commit()
        id = self.cursor.lastrowid
        endereco.id = id
        return endereco.__dict__

    def update(self,endereoco:EnderecoModel):
        self.cursor.execute("UPDATE 01_MDG_ENDERECO SET LOGRADOURO = '{}', NUMERO = '{}' , COMPLEMENTO = '{}' , BAIRRO = '{}', CIDADE = '{}', CEP = '{}' WHERE ID ='{}' ".format(endereoco.logradouro,endereoco.numero,endereoco.complemento,endereoco.bairro,endereoco.cidade,endereoco.cep,endereoco.id))
        self.connection.commit()
        return endereoco.__dict__

    def remove(self,id):
        self.cursor.execute("DELETE FROM 01_MDG_ENDERECO WHERE ID = {} ".format(id))
        self.connection.commit()
        return 'Removendo a pessoa de id: {}'.format(id)