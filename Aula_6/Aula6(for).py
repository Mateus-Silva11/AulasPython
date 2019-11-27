# for

# for simples usando range com incremento padrao de 1
for i in range(0,10):
    print(f'{i}-Eu te amo')
# for usandos usando m incremento 2
for i in range(0,100,2):
    print(f'{i}-Eu te amo')
        
lista = ['Mateus','Matheus','Marcela','Nicole','tonho','Pablo' ]    

for i in range(0,6):
    print(lista[i])


lista.append('Natan')
for i in lista:
    print(i)

n = 10
for i in range(0,6):
    print(f'{i} x {n} = {i*n} ')