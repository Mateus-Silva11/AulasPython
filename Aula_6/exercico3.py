#--- Exercício 3 - Foreach
#--- Escreva programa que leia as notas (4) de 10 alunos
#--- Armazene as notas e os nomes em listas
#--- Imprima:
#           1- O nome dos alunos 
#           2- Média do aluno
#           3- Resuldo (Aprovado>=7.0)

notas =[]
nomes = []
media = 0
a = 0
b = 1
c = 2
d = 3

for d in range(1,11):   
    aluno = [input(f'Informe o {d} Nome')]
    nomes.append(aluno)
    for i in range(1,5):    
        nota = [float(input(f'Informe a {i} Nota'))]
        notas.append(nota)
        
for alunos in nomes:

     media = (notas[a]+notas[b]+notas[c]+notas[d])/4
     print(f'\nNome: {alunos}')
     print(f'Média: {media}')
     if media >= 7:
          print('Aprovado!')
     else:
          print('Reprovado!')
    
     a = a+4
     b = b+4
     c = c+4
     d = d+4