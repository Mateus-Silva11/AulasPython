lista_terminal_inicial = ['Piloto','Chefe de serviço','Policial','1_Oficial','2_Oficial','1_Comissaria','2_Comissaria','Bandido']
lista_pessoas_aviao = []


#Dados da primeira viagem

print('Primeira viagem')
print(f'Pessoas pronta para o embarque {lista_terminal_inicial}')
print(f'Piloto e chefe de serviço deveram embarca no frotwu')
lista_pessoas_aviao.append('Piloto')
lista_pessoas_aviao.append('Chefe de serviço')
print(f'Pessoas embarcadas no Fortwo {lista_pessoas_aviao}')
lista_terminal_inicial.remove('Piloto')
lista_terminal_inicial.remove('Chefe de serviço')
print(f'Pessoas que ficaram no terminal {lista_terminal_inicial} ')

#Dados da segunda viagem 
lista_pessoas_aviao.clear()
print('Segunda viagem ')
lista_terminal_inicial.append('Piloto')
print(f'Pessoas pronta para o embarque {lista_terminal_inicial} ')
lista_pessoas_aviao.append('Policial')
lista_pessoas_aviao.append('Bandido')
print(f'Pessoas embarcadas no fortwo {lista_pessoas_aviao}')
lista_terminal_inicial.remove('Policial')
lista_terminal_inicial.remove('Bandido')
print(f'Pessoas que ficaram no terminal {lista_terminal_inicial}')

#Dados da terceira viagem
lista_pessoas_aviao.clear()
print('Terceira viagem')
lista_terminal_inicial.append('Chefe de serviço')
print('')