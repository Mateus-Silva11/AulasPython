# Aula 18 - 03-11-2019

# A lista a seguir possui mais uma lista interna, a lista de preços.
# A lista de preços possui 3 sublistas dentro dela com os preços dos produtos.
# para exemplificar, o preço do mamão é de 10.00 - alface crespa é de 2.99 e o feijão 9.0

lista = [
          ['frutas','verduras','legumes','preço'],
          ['mamão','abacaxi','laranja','uva','pera','maçã','vergamota'],
          ['alface crespa', 'alface 1lisa','rucula','almerão','repolho','salsinha',],
          ['feijão', 'erviha', 'lentilha','vagem','feijão branco','gão de bico','soja'],
          [ 
            
            [10.00, 2.56, 5.25, 9.5, 10.05, 15, 5.75], [2.99, 2.95, 3.5, 3.25, 5.89, 2.9, 2.5],
            [9.0, 5.0, 7.5, 1.75, 10.9, 5.99, 3.55] 
          
          ]
        ]

# Será solicitado o preço de alguns produtos. para imprimir deve ser por f-string refrenciando o nome com o preço 
# da seguinte forma: "O preço do {} é R$ {}"

print('1: imprima o valor do abacaxi')

print(lista[4][0][1])

print('2: imprima o valor da rucula')

print(lista[4][1][2])

print('3: imprima o valor da laranja')

print(lista[4][0][2])

print('4: imprima o valor do repolho')

print(lista[4][1][4])

print('5: imprima o valor do feijão')

print(lista[4][2][0])

print('6: imprima o valor do feijão branco')

print(lista[4][2][4])

print('7: imprima o valor da vergamota')

print(lista[4][0][6])

print('8: imprima o valor da alface lisa')

print(lista[4][1][1])

print('9: imprima o valor do mamão')
print('10: imprima o valor da soja')
print('11: imprima o valor da lentilha')
print('12: imprima o valor da uva')
print('13: imprima o valor da vagem')
print('14: imprima o valor do almeirão')
print('15: imprima o valor da ervilha')
print('16: imprima o valor da maçã')

