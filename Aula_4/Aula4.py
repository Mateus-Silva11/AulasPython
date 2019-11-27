#Aula 4 
# FAzer um ptograma que leia 2 numeors do console
# Realize as 4 operações matematica
#  Imprima o resiltado das operações
#  Diga qual o numero é o maior dos dois nunmeros

numero1 = int(input('Informe o priemiro Numero: '))
numero2 = int(input('Informe o priemiro Numero: '))

print('='*50 , '\n'*2)
resultado = numero1+numero2
print(f'{numero1} + {numero2} é igual a: {resultado}')
resultado = numero1/numero2
print(f'{numero1} / {numero2} é igual a: {resultado}')
resultado = numero1-numero2
print(f'{numero1} - {numero2} é igual a: {resultado}')
resultado = numero1*numero2
print(f'{numero1} * {numero2} é igual a: {resultado}')

print('\n'*2 ,'='*50)

if numero1 > numero2 :
    print('='*50, '\n')
    print(f'Maioir Numeoro {numero1}')
    print('\n' ,'='*50)
elif numero1 == numero2 :
    print('='*50, '\n')
    print('Numero são iguais')
    print('\n','='*50)
else:   
    print('='*50, '\n')
    print(f'Maioir Numeor {numero2}')
    print('\n' ,'='*50) 