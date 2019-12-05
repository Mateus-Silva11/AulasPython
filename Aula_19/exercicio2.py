# Aula 19 - 04-12-2019
# Lista com for e metodos

cab = ['nome', 'telefone', 'email', 'idade']

pess = [['Alex', 'Paulo', 'Pedro', 'Mateus', 'Carlos', 'João', 'Joaquim'],
        ['4799991', '4799992', '4799993', '4799994',
         '4799995', '4799996', '4799997'],
        ['a@a.com', 'b@b.com', 'c@c.com', 'd@d.com',
         'e@e.com', 'f@f.com', 'g@g.com'],
        ['18', '25', '40', '16', '15', '19', '17']
        ]


# 1 - Usando estas 2 listas, fazer uma função que crie retorne uma lista com dicionários
# com os dados das pessoas com idade maior ou igua a 18 anos

def verificar():
    nomes = pess[0]
    telefone = pess[1]
    e_mail = pess[2]
    idades = pess[3]
    lista_dados = []
    for i in range(len(idades)):
        if int(idades[i]) >= 18:
            dicionario = {'Nome': nomes[i], 'Telefone': telefone[i], 'e-mail': e_mail[i], 'Idade': idades[i]}
            lista_dados.append(dicionario)
    return lista_dados

print(verificar())


#  2 - Imprima a lista resultante com um for imprimindo um dicionário em cada linha
# (não prescisa usar o f-string, .format())
nomes = pess[0]
telefone = pess[1]
e_mail = pess[2]
idades = pess[3]

lista_dados = []

for linha in range(len(pess[-1])):
    dicionario = {'Nome': nomes[linha], 'Telefone': telefone[linha], 'e-mail': e_mail[linha], 'Idade': idades[linha]}
    lista_dados.append(dicionario)

#  3 - Imprima a lista resultante com um for imprimindo um dicionário em cada linha
# (usando o f-string)


for i in lista_dados:
    print(f" Nome: {i['Nome']}  - Telefone: {i['Telefone']} - E-mail: {i['e-mail']}  - Idade: {i['Idade']} ")
