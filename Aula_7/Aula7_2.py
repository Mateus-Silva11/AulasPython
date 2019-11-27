# dicionario_bandas = {}
# dicionario_bandas['Nome'] = 'Mateus'
# dicionario_bandas['Nome'] = 'Dejavu'

# print(dicionario_bandas)


dicionario_pessoa = {'Nome': '', 'Sobrenome':'', 'CPF': '', 'RG':''}
lista_pessoa = []
for i in range(1,11):
    dicionario_pessoa['Nome'] = input('Digite o Nome')
    dicionario_pessoa['Sobrenome'] = input('Digite o Sobrenome')
    dicionario_pessoa['CPF'] = input('Digite o CPF')
    dicionario_pessoa['RG'] = input('Digite o RG')
    lista_pessoa.append(dicionario_pessoa)