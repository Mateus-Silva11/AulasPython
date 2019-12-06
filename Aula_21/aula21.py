controle = 'n'

while controle != 's':
    try:    
    
        n1 = int(input('Informe um numero'))
        n2 = int(input('Informe outro numero'))
    
    except ValueError:
        print('Digite o Numero Novamente (obs: Nuemro inteiro)')

    else:    
        print(f'A soma entre {n1} + {n2} é = {n1+n2}')  
        print(f'A multiplicação entre {n1} * {n2} é = {n1*n2}')
        print(f'A divição entre {n1} / {n2} é = {n1/n2}')
        print(f'A subtração entre {n1} - {n2} é = {n1-n2}')
        controle = input('Desseja Parar?')

# while True:
        
#     try:
#         numero = int(input('Digite um Numero'))
#     except ValueError:
#         print('Você digitou o numero errado seu animal')
#     else:
#         print('Salve')
#         break
  