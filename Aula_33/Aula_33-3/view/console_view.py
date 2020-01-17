import sys
sys.path.append('C:/Users/900148/Desktop/GitHub/AulasPython/Aula_33/Aula_33-3')
from controller.pessoa_controller import PessoaController
from controller.endereco_controller import EnderecoController

pc = PessoaController()
ec = EnderecoController()
print('++++++++++++++++++++++++PESSOA++++++++++++++++++++++++++++++')
for p in pc.listar_todos():
   print(p)

print('++++++++++++++++++++++++++++++++++++++++++++++++++++++')

print('+++++++++++++++++++++++ENDEREÇO++++++++++++++++++++++++++++++')
for e in ec.listar_todos():
    print(e)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++')