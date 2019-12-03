def cadastro_cliente(nuemro):
    lista_cliente = [ 'cod_cliente' , 'cpf' , 'nome_completo' , 'data_nasc' , 'estado' , 'cidade' , 'cep' , 'bairro' , 'rua', 'numero_casa' , 'complemento'  ]
    lista_dados = []

    for j in range(nuemro):
        dicionario_dados = {}  
        for i in lista_cliente:
            dicionario_dados[i]=input(f'{i}:')
            # dado1 = input(f'{i}: ')  
        lista_dados.append(dicionario_dados)
    return lista_dados   

nuemro = int(input('Digite nuemro de cadastros: '))
print(f'{cadastro_cliente(nuemro)}')

#Criar um função para salvar em arquivo 

arquivo = open('Aula_17/Clientes.txt','a')
for cliente in arquivo :


arquivo.close()