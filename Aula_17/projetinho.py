menu = ''' 

######################################################################
#                  I Festival de Cerveja em Ituroró                  #
######################################################################

1- Cadastro de Cliente
2- Ver Clientes Cadastrados
3- Cadastro de Produtos
4- Ver Produtos Cadastrados
5- Vendas
6- Relatório de Vendas
7- Sair

Digite a opcção desejada:
'''
while True:
    opcao = input(menu)
    if opcao == '1':
        print('Cadastro de Cliente')
    elif opcao == '2':
        print('Ver Clientes Cadastrados')
    elif opcao == '3':
        print('Cadastro de Produtos')
    elif opcao == '4': 
        print('Ver Produtos Cadastrados')  
    elif opcao == '5':
        print('Vendas') 
    elif opcao == '6':
        print('Relatório de Vebdas')
    elif opcao == '7':
        print('Sair')
        break
    else:
        print('Valor invalido')
          