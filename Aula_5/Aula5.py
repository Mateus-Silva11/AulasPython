#  cRIE UM PROGRAMA QUE LEIA 4 NOTAS
#  Imprima a maior nota
#  Imprama a menor nota
#  Imprima a media
#  Imprima se o aluno foi aprovado ou reprovado (media 7.0)

n1 = float(input('Informe a Primeira Nota'))
n2 = float(input('Informe a Segunda Nota'))
n3 = float(input('Informe a terceira Nota'))
n4 = float(input('Informe a Quarta Nota'))

if n1 > n2 and n1 > n3 and n1 > n4:
    print(f'Maior Nota: {n1}')
elif n2 > n1 and n2 > n3 and n2 > n4:
    print(f'Maior Nota: {n2}')
elif n3 > n1 and n3 > n2 and n3 > n4: 
    print(f'Maior Nota: {n3}')
else :    
    print(f'Maior Nota: {n4}')

#Arruma depois
if n1 < n2:
    print(f'Menor Nota: {n1}')
elif n2 < n3:
    print(f'Menor Nota: {n2}')
elif n3 < n4:  
    print(f'Menor Nota: {n3}')
else :    
    print(f'Menor Nota: {n4}')   


media = (n1+n2+n3+n4)/4
print(f'Media do Auno é: {media}')

if media >= 7:
    print(f'Aluno Aprovado media do aluno: {media}')
else:
    print(f'Aluno Reprovado media do aluno: {media}')    