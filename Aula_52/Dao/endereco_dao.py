from Aula_52.Model.endereco_model import EnderecoModel
from Aula_52.Dao.base_dao import BaseDao

class EnderecoDao(BaseDao):
    def __init__(self):
        super().__init__("01_MDG_ENDERECO")

    def listar_todos(self):
        tuplas = super().listar_todos()
        lista = []
        for e in tuplas:
            model = EnderecoModel(e[1], e[2], e[3], e[4], e[5], e[6], e[0])
            lista.append(model.__dict__)
        return lista

    def buscar_por_id(self, id):
        tupla = super().buscar_por_id(id)
        model = EnderecoModel(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[0])
        return model.__dict__

    def inserir(self, model: EnderecoModel):
        self.cursor.execute("""INSERT INTO {}  
                            (
                                LOGRADOURO,
                                NUMERO,
                                COMPLEMENTO,
                                BAIRRO,
                                CIDADE,
                                CEP
                            )VALUES
                            (
                                '{}',
                                '{}',
                                '{}',
                                '{}',
                                '{}',
                                '{}'
                            )
                            """.format(self.tabela, model.logradouro, model.numero, model.complemento, model.bairro, model.cidade, model.cep ))
        self.conexao.commit()
        model.id = self.cursor.lastrowid
        return model.__dict__

    def alterar(self, model: EnderecoModel):
        self.cursor.execute(""" UPDATE {}
                            SET 
                                LOGRADOURO = '{}',
                                NUMERO = '{}',
                                COMPLEMENTO = '{}',
                                BAIRRO = '{}',
                                CIDADE = '{}',
                                CEP = '{}'
                            WHERE ID = {}
                            """.format(self.tabela, model.logradouro, model.numero, model.complemento, model.bairro, model.cidade, model.cep, model.id ))
        self.conexao.commit()
        return model.__dict__

    def deletar(self, id):
        self.cursor.execute(""" DELETE FROM {}
                                WHERE ID = {}
                            """.format(self.tabela, id))
        self.conexao.commit()
        return "Endereco de id {} deletado com sucesso".format(id)
