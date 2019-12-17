# Aula 21 - 16-12-2019
#Funções para listas

from geradorlista import lista_simples_int

from random import randint

lista1 = lista_simples_int(randint(5,100))
lista2 = lista_simples_int(randint(5,75))
lista3 = lista_simples_int(randint(5,70))


# 1) Com as listas aleatórias (lista1,lista2,lista3) e usando as funções para listas,
# f-string, responda as seguintes questões:


# 1.1) Qual é o tamanho da lista1?
print(f"Tamanho da lista1 : {len(lista1)}")

# 1.2) Qual é o maior valor da lista2?

print(f"Maior valor da lista2 : {max(lista2)}")

# 1.3) Qual seria a soma do maior valor com o menor valor da lista2?

print(f"A soma entre o maior valor da Lista2: {max(lista2)} e o menor valor da lista2: {min(lista2)} é de : {max(lista2)+min(lista2)}")

# 1.4) Qual é a média aritmética da lista1?

print(f"A media aproximada da lista1 é {round(sum(lista1)/len(lista1),2)} ")

# 1.5) Qual o valor da soma de todas as listas e a soma total delas?
# quero que mostre a soma individual (por lista) e a soma total de todas elas (soma das somas das listas)

print(f'A soma da lista1: {sum(lista1)}. A soma da lista2: {sum(lista2)}. A soma da lista3: {sum(lista3)}. Valor total: {sum(lista1)+sum(lista2)+sum(lista3)}')

# 1.6) Usando o f-string, imprima todos os valores da lista1 um de baixo do outro.

for elemento in lista1:
    print(f'Elementos da lista1: {elemento}')

# 1.7) Com a indexação e f-string, mostre o valor das posições 5, 9, 10 e 25 de cada lista.
# trate para evitar o erro: IndexError

try:

    print(f'Posições da lista1: {lista1[5]}, {lista1[9]}, {lista1[10]} e {lista1[25]} ')
    print(f'Posições da lista2: {lista2[5]}, {lista2[9]}, {lista2[10]} e {lista2[25]} ')
    print(f'Posições da lista3: {lista3[5]}, {lista3[9]}, {lista3[10]} e {lista3[25]} ')

except IndexError:
    print('erro de índice')    

# 1.8) Mostre qual das listas tem mais itens (lembre-se, as listas são randômicas, não há como prever o 
# tamanho delas).

if len(lista1) > len(lista2):
    print(f'A lista1 é a com maior itens')
elif len(lista1) < len(lista2) and len(lista2) > len(lista3):
    print(f'A lista2 é a com maior itens') 
else:
    print('a lista3 é a maior')

# 1.9) Some os maiores números de todas as listas e subtraia pelo menor número dos menores valores das listas.
# Para obter o menor valor, pegue o menor valor das listas e veja qual deles é o menor e use ele.



# 1.10) Pegue o maior valor de todas as listas e some com o menor valor de todas as listas

print(f'{max(lista1)+min(lista1)}') 
print(f'{max(lista2)+min(lista2)}')
print(f'{max(lista3)+min(lista3)}')


