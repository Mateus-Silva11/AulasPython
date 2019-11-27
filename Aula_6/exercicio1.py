# Exercico 1 - listas 
# Escreva program que leia a nome de 10 alunos
#  Armezene os nomes em uma lista 
#  Imprema a lista
nomes =[]
for i in range(1,11):
    nome = [input(f'Informe o {i} Nome')]
    nomes.append(nome)

for d in nomes:
    print(f' Nomes informados {d}')