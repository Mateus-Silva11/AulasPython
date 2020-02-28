# Uma matriz A consistindo de N inteiros é fornecida.
# A rotação da matriz significa que cada elemento é deslocado para a direita por um índice e o último elemento da matriz é movido para o primeiro lugar.
# Por exemplo, a rotação da matriz A = [3, 8, 9, 7, 6] é [6, 3, 8, 9, 7]
# (os elementos são deslocados para a direita por um índice e 6 é movido para o primeiro lugar).

# O objetivo é girar os tempos AK da matriz; isto é, cada elemento de A será deslocado para o K tempo certo.
# Escreva uma função:
# solução def (A, K)
# que, dada uma matriz A que consiste em N números inteiros e um número inteiro K, retorna a matriz A girada K vezes.
# Por exemplo, dado
#     A = [3, 8, 9, 7, 6]
#     K = 3
# a função deve retornar [9, 7, 6, 3, 8]. Foram realizadas três rotações:
#     [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
#     [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
#     [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
# Por outro exemplo, dado
#     A = [0, 0, 0]
#     K = 1
# a função deve retornar [0, 0, 0]
# Dado
#     A = [1, 2, 3, 4]
#     K = 4
# a função deve retornar [1, 2, 3, 4]
# Assuma isso:
# N e K são inteiros dentro do intervalo [ 0 .. 100 ];
# cada elemento da matriz A é um número inteiro dentro do intervalo [ -1.000 .. 1.000 ].
# Na sua solução, concentre-se na correção . O desempenho da sua solução não será o foco da avaliação.

A = [3, 8, 9, 7, 6]
K = 15
def solution(A,K):
    for i in range(K):
        b = A[-1]
        A.insert(0, b)
        A.pop()
    return A
print(solution(A,K))