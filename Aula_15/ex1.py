def salvar_pessoa(pessoa_dicionario):
    arquivo = open('teste2.txt','a')
    arquivo.write(f" {pessoa_dicionario['Nome']}; {pessoa_dicionario['Sobrenome']}; {pessoa_dicionario['Idade']}  \n")
    arquivo.close()

def leitura():
    lista = []
    arquivo = open('teste2.txt','r')
    for linha in arquivo:
        linha = linha.strip()
        lista_linha = linha.split(';')
        pessoa  = {'Nome':lista_linha[0] , 'Sobrenome':lista_linha[1] , 'Idade':lista_linha[2] }
        lista.append(pessoa) 
    arquivo.close()
    return lista

nome = input('Informe seu nome: ')
sobrenome= input('Informe seu sobrenome: ')
idade = int(input('Digite a idade: '))

pessoa  = {'Nome':nome , 'Sobrenome':sobrenome , 'Idade':idade }


salvar_pessoa(pessoa)

for p in leitura():
    print(f"{p['nome']} - {p['Sobrenome']} - {p['Idade']} ")
