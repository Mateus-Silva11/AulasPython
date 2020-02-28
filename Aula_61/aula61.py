# Um espaço binário dentro de um número inteiro positivo N é qualquer sequência máxima de zeros consecutivos
# que está rodeado por 1 dos dois lados na representação binária de N.
#
# Por exemplo, o número 9 tem representação binária 1001 e contém uma lacuna binária de comprimento 2.
# O número 529 tem representação binária 1000010001 e contém duas lacunas binárias:
# um de comprimento 4 e um de comprimento 3.
# O número 20 tem representação binária 10100 e contém um espaço binário de comprimento 1.
# O número 15 tem representação binária 1111 e não possui lacunas binárias.
# O número 32 tem representação binária 100000 e não possui lacunas binárias.
#
# Escreva uma função:
#
# solução def (N)
#
# que, dado um número inteiro positivo N, retorna o comprimento de seu maior intervalo binário.
# A função deve retornar 0 se N não contiver um espaço binário.
#
# Exemplo, dado N = 1041, a função deve retornar 5,
# porque N tem representação binária 10000010001 e, portanto, seu maior intervalo binário tem o comprimento 5.
#
# Dado N = 32, a função deve retornar 0, porque N tem representação binária '100000'
# e, portanto, sem lacunas binárias.
# numero = int(input("Informe um Numero"))

def binarygap(numero):
    numero = bin(numero)
    print(numero)
    maior_gap = 0
    x = 0
    for i in numero:
        if i == "1":
            x = numero.index(i) + 1
            gap = 0
            while numero[x] < "1":
                gap += 1
                x += 1
            if gap > maior_gap:
                maior_gap = gap
    print('{}'.format(maior_gap))

binarygap(numero)
