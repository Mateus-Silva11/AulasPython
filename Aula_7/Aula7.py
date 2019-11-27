#listas
nome2 = 'AA'
sob = 'bb'
lista_notas = [12, 30, 40, 90]

dicionario = {'Nome' : nome2 , 'Sobrenome': sob }
print(dicionario)
print(dicionario['Sobrenome'])

nome = 'Matues'
lista_notas = [8, 5 , 4, 9]


media = sum(lista_notas)/ len(lista_notas)

situacao = 'reprovado'

if media >=7:
    situacao = 'Aprovado'

dicionario_alunos = {'Nome': nome, 'Lista_Notas':lista_notas, 'Media':media , 'Situacao': situacao}

print(f"{dicionario_alunos['Nome']} - {dicionario_alunos['Lista_Notas']} - {dicionario_alunos['Media']} - {dicionario_alunos['Situacao']}  ")
