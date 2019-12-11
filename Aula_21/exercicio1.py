# Aula 21 - 06-12-2019
# Como Tratar e Trabalhar Erros!!!

# 1 - Crie um arquivo que leia 2 números inteiros e imprima a soma, 
# multiplicação, divisão e subtração com uma f-string.

# 2 - Crie um while que pergunte se deseja continuar. Se digitar 's' o
# programa termina.

#################### até aqui tudo bem! ##########################

# 3 - faça um tratamento de exceção para que ao digitar o valor que 
# não seja inteiro, ele avise o usuário para ele digitar denovo.
# 4 - Faça outro tratamento de exceção para evitar que divida um numero
# por zero.


controle = 'n'

while controle != 's':
    try:    
    
        n1 = int(input('Informe um numero'))
        n2 = int(input('Informe outro numero'))
        print(f'A soma entre {n1} + {n2} é = {n1+n2}')  
        print(f'A multiplicação entre {n1} * {n2} é = {n1*n2}')
        print(f'A divição entre {n1} / {n2} é = {n1/n2}')
        print(f'A subtração entre {n1} - {n2} é = {n1-n2}')
    
    except ValueError:  
       print('Digite o Numero Novamente (obs: Nuemro inteiro)')
    
    except ZeroDivisionError:  
        print('Impossivel fazer a divição com 0')

    else:      
        controle = input('Desseja Parar?')
