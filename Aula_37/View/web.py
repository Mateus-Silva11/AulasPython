from flask import Flask, render_template, request, redirect
import sys
sys.path.append(r'C:\Users\900148\Desktop\GitHub\AulasPython\Aula_37')
from Controller.squad_controller import SquadController
from Model.squad import *

app = Flask(__name__)
squad = SquadController()
nome = 'Cadastros'

@app.route('/')
def inicio():
    return render_template('index.html', titulo_app = nome )

@app.route('/listar')
def listar():
    squad1 = SquadController()
    squad = squad1.listar_todos()
    for i in squad:
        print(i)
    return render_template('listar.html', titulo_app = nome, lista = squad)

@app.route('/cadastrar')
def cadastrar():
    squad = SquadController()
    if 'idSquad' in request.args:
        idSquad = request.args['id']
        squad1 = SquadController()
        squad = squad1.buscar_por_id(idSquad)

    return render_template('cadastrar.html', titulo_app = nome, lista = squad)

@app.route('/excluir')

def excluir():
    idSquad = int(request.args['id'])
    SquadController.deletar(idSquad)
    return redirect('/listar')

@app.route('/salvar')
def salvar():
    squad = Squad()
    squad.idSquad = request.args['idSquad']
    squad.Nome = request.args['Nome']
    squad.NumeroPessoas = request.args['Descricao']
    squad.LinguagemBackEnd = request.args['LinguagemBackEnd']
    squad.FrameworkFrontEnd = request.args['FrameworkFrontEnd']
    if squad.idSquad == 0:
        SquadController.salvar(squad)
    else:
        SquadController.alterar(squad)
    return redirect('/listar')

app.run(debug=True)

