# Aula 6 [Listas,vetores]
#conhecito de lista pode usar qualquer tipo de dados esse conjuto de dados dentro de uma unica variavel

#listas

#inicialização de uma variel do tipo lista
lista1 = []

#inicialização de uma variel lista, com elementos
lista2 = ['Marcela', 'Nicole','*Matheus']

#lista de inteiros
lista3 = [1,2,3,5]

#lista de tipos diferestes.
lista4 =[1, 'Mateus', 23.5]

#Impressao das listas criadas
print(lista1)
print(lista2)
print(lista3)
print(lista4)
# ---- Adicionando elementeos em uma lista ja criada

lista1.append(lista2)
lista1.append(lista3)

# Criação de lista com dados vindos da função Input

lista_duvida = [input('aaaaa'), input('sdsdsdsdsdss')]
print(lista_duvida)

#Recuperando um dado de uma posição especifica  da lista
posicao = int(input('Digite a posicao'))
print(lista2[posicao-1])



