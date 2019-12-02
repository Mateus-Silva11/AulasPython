lista_cliente = [ 'cod_cliente' , 'cpf' , 'nome_completo' , 'data_nasc' , 'estado' , 'cidade' , 'cep' , 'bairro' , 'rua', 'numero_casa' , 'complemento'  ]
lista_dados = []

nuemro = int(input('Digite nuemro de cadastros: '))
nuemro = nuemro + 1

for j in range(1,nuemro):
    dicionario_dados = {}
    
    for i in lista_cliente:
        dicionario_dados[i]=input(f'{i}:')
        # dado1 = input(f'{i}: ')  

    lista_dados.append(dicionario_dados)

print(dicionario_dados)
print(lista_dados)