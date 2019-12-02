menu ='''
######################################################################
#                  Sla  a vida é Boa                                 #
######################################################################

1- Cadastrar uma Banda
2- Cadastrar um Album
3- Cadastrar uma Musica
4- Sair

Digite o Opção desejada :

 '''

lista_musica = []
lista_album = []
lista_banda = []

while True :
    op = input(menu)        

    if op == '1':
        
        print('Cadastro uma Banda')
        lista_banda.append(input('Informe o Nome da Banda'))
        

    elif op == '2':
       
        print('Cadastro de um Album')
        lista_album.append(input('Informe o Nome do Album'))
        
   
    elif op == '3':
        
        lista_musica.append(input('Informe o Nome da Musica'))
        
    
    elif op == '4':      
        
        print('Sair Obg Pela Prefencia')
        print(f'Bandas Cadastradas : {lista_banda} - Albuns Cadastrados: {lista_album} - Musica Cadastradas : {lista_musica}  ')
        break

    else:
        print('Valor Invalido')    

