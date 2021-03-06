from flask_restful import Resource
from flask import request
from Aula_41.Dao.endereco_dao import EnderecoDao
from Aula_41.Model.endereco_model import EnderecoModel
class EnderecoController(Resource):
    def __init__(self):
        self.dao = EnderecoDao()

    def get(self, id=None):
        if id:
            return self.dao.get_by_id(id)
        return self.dao.list_all()
    def post(self):
        logradouro = request.json['logradouro']
        numero = request.json['numero']
        complemento = request.json['complemento']
        bairro = request.json['bairro']
        cidade = request.json['cidade']
        cep = request.json['cep']
        endereco = EnderecoModel(**request.json)
        return self.dao.insert(endereco)
    def put(self,id):
        logradouro = request.json['logradouro']
        numero = request.json['numero']
        complemento = request.json['complemento']
        bairro = request.json['bairro']
        cidade = request.json['cidade']
        cep = request.json['cep']

        endereco = EnderecoModel(logradouro=logradouro, numero=numero,complemento=complemento,bairro=bairro,cidade=cidade,cep=cep)
        return self.dao.update(endereco)

    def delete(self, id):

        return self.dao.remove(id)


