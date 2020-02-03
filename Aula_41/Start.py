from flask import Flask
from flask_restful import Api
from Aula_41.Controllers.pessoa_controller import PessoaController
from Aula_41.Controllers.endereco_controller import EnderecoController

app = Flask(__name__)
api = Api(app)
#Pessoa API
api.add_resource(PessoaController,'/api/pessoa', endpoint='pessoas')
api.add_resource(PessoaController,'/api/pessoa/<int:id>', endpoint='pessoa')
#Endereço API
api.add_resource(EnderecoController,'/api/endereco', endpoint='enderecos')
api.add_resource(EnderecoController,'/api/endereco/<int:id>', endpoint='endereco')
@app.route('/')
def inicio():
    return 'Bem vindo a API Pessoa / Endereco'

app.run(debug=True, port=80)
