from flask_restful import Resource
from flask import request

from Aula_52.Model.endereco_model import EnderecoModel
from Aula_52.Dao.endereco_dao import EnderecoDao

class EnderecoController(Resource):
    def __init__(self):
        self.dao = EnderecoDao()

    def get(self, id=None):
        if id:
            return self.dao.buscar_por_id(id)
        return self.dao.listar_todos()

    def post(self):
        logradouro = request.json['logradouro']
        numero = request.json['numero']
        complemento = request.json['complemento']
        bairro = request.json['bairro']
        cidade = request.json['cidade']
        cep = request.json['cep']
        model = EnderecoModel(logradouro, complemento, numero, bairro, cidade, cep)
        return self.dao.inserir(model)

    def put(self, id):
        logradouro = request.json['logradouro']
        numero = request.json['numero']
        complemento = request.json['complemento']
        bairro = request.json['bairro']
        cidade = request.json['cidade']
        cep = request.json['cep']
        model = EnderecoModel(logradouro, complemento, numero, bairro, cidade, cep, id)
        return self.dao.alterar(model)

    def delete(self, id):
        return self.dao.deletar(id)