# Aula 19 - 04-12-2019
# Lista com for e metodos

# Como comer um gigante.... é com um pedaço de cada vez.
# Na hora de fazer este exercicio, atentar para 

# Com o arquivo de cadastro.txt onde possui os seguintes dados: codigo cliente, nome, idade, sexo, e-mail e telefone
# 1 - Crie um metodo que gere e retorne uma lista com bibliotecas com os dados dos clientes
# 2 - Com a lista do exercicio 1, separe os adultos dos menores de idade e salve em um arquivo .txt cada.
# Esta função tambem retornar uma lista com a biblioteca dos maiores de idades.
# 3 - Crie uma função que conte quantas mulheres e quantos homens tem na lista. Salve cada um em um arquivo diferente.
# 4 - Faça uma função de consulta de cadastro. A função deve receber o valor do código do cliente e deve imprimir na 
# tela os dados do cliente com f-string usando a lista do exercicio 1
#  4.1 - A pesquisa deve aparecer uma frase para as seguintes condições:
#           Mulheres até 16 anos: "Ola {nome}! Você quer aproveitar nosso Tikito sabor Gloss? É uma delicia!""
#           Mulheres acima de 16 a 18 anos: "Olá {nome}! Quer experimentar nosso refigerante sabor alegria! O seu 
#                                            cruch vai adorar!"
#           Mulheres acima de 18:  "Olá {nome}! Já experimentou nossa bebida a base de tequila? Baixo tero alcoolico
#                                                com o dobro de sabor!!!"
#           Homens até 16 anos: "Ola {nome}! Você quer aproveitar nosso Tikito sabor Meleka? É uma delicia!""
#           Homens acima de 16 a 18 anos: "Olá {nome}! Quer experimentar nosso refigerante sabor Corriga de carros!  
#                                          A sua amada vai adorar!"
#           Homens acima de 18:  "Olá {nome}! Já experimentou nossa cerveja? alto teor alcoolico
#                                                com o dobro do amargor!!!"
#      Lembre-se: É importante que apareça a frase. Pois a mesma será encaminhada por e-mail pela equipe de marketing


#1 - Crie um metodo que gere e retorne uma lista com bibliotecas com os dados dos clientes
def ler():
    arquivo_principal = open('Aula_19/cadastro.txt','r')
    lista_dados = []
    for linha in arquivo_principal:
        linha_limpa = linha.strip()
        linha_lista = linha_limpa.split(';')
        dicionario = {'Id':linha_lista[0] , 'Nome':linha_lista[1] , 'Idade': linha_lista[2], 'Sexo':linha_lista[3] , 'E-mail':linha_lista[4] ,'Telefone':linha_lista[5] }
        lista_dados.append(dicionario)
    arquivo_principal.close()
    return lista_dados

#2 - Com a lista do exercicio 1, separe os adultos dos menores de idade e salve em um arquivo .txt cada.
lista_ler = ler()
arquivo_maior = open('Aula_19/Maiores.txt','a')
arquivo_menor = open('Aula_19/Menores.txt','a')

for dicionario in lista_ler: 
    if int(dicionario['Idade'])>= 18:
        arquivo_maior.write(f"{dicionario['Id']};{dicionario['Nome']};{dicionario['Idade']};{dicionario['Sexo']};{dicionario['E-mail']};{dicionario['Telefone']}\n")
    else:
       arquivo_menor.write(f"{dicionario['Id']};{dicionario['Nome']};{dicionario['Idade']};{dicionario['Sexo']};{dicionario['E-mail']};{dicionario['Telefone']}\n")

arquivo_maior.close()        
arquivo_menor.close()

# 3 - Crie uma função que conte quantas mulheres e quantos homens tem na lista. Salve cada um em um arquivo diferente.
# def Contar():
#     cont_m = 0
#     cont_f = 0
#     for dicionario in lista_ler:
#         if dicionario['Sexo']== 'm':
#             cont_m += 1
#             print(f' Homem: {cont_m}')
#         else:
#             cont_f += 1
#             print(f' Mulher {cont_f}')
# Contar()
def a(lista_ler):
    lista = []
    for dicionario in lista_ler:
        if dicionario['Sexo'] == 'm':
            a=dicionario['Sexo'].count('m')
            lista.append(a)
            print(len(lista))

a(lista_ler)            