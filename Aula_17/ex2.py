from random import randint

aleatorio = randint(1,100)
n= 0

while n != aleatorio:
    n = int(input('Informe um numero entre 1 a 100'))

    if n < aleatorio:
        print(f'Numero {n} e Menor')
        print('Voce errou')
    
    elif n > aleatorio:
        print(f'Numero {n} é Maior')
        print('Voce errou')
    
    else:
       
        print('='*50 , '\n')
        print('\t','Voce acertou gato ')
        print('\n')
        print('='*50)    
       