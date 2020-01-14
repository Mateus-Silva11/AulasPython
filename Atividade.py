lista_terminal_inicial = ['Piloto','Chefe','Policial','1_Oficial','2_Oficial','1_Comissaria','2_Comissaria','Bandido']
lista_pessoas_aviao = []

piloto = input('Informe quem ira pilotar a fortwu 1) Piloto 2)Cheve de serviço')
hsaida = input('Informe a hora de saida')
hchegada = input('Informe a hora de chegada')



if piloto == '1':	
       
    print(f'Fortwu saio as : {hsaida} hrs do terminal')
    lista_pessoas_aviao.append(lista_terminal_inicial[0])
    lista_pessoas_aviao.append(lista_terminal_inicial[1])
    print('Quem deverar Embarca peimeiro com o Piloto e o chefe de serviço')
    print('O piloto deverar levar o chefe de serviço e deverar retornar para o terminal iniciall ')
    print(f'Pessoa do estão embarcadas no fortwu{lista_pessoas_aviao}')
    lista_terminal_inicial.remove('Piloto')
    lista_terminal_inicial.remove('Chefe')
    print(f'Pessoa que ficaram no ternimal inicial {lista_terminal_inicial}')
    print(f'fortwu chego as : {hchegada} hrs ')
    lista_pessoas_aviao.remove('Chefe')
    print(f'O {lista_pessoas_aviao} Retorno ao terminal inicial')

   

elif piloto == '2':
    lista_pessoas_aviao=[]
    print(f'Fortwu saio as : {hsaida} hrs do terminal')
    lista_pessoas_aviao.append(lista_terminal_inicial[1])
    lista_pessoas_aviao.append(lista_terminal_inicial[0])        
    print('Quem deverar embarca primeiro com o Cheve de serviço deverar ser o Piloto ')
    print('O piloto deverar levar o chefe de serviço e voltar ao terminal ')
    print(f'Pessoa do estão embarcadas no fortwu{lista_pessoas_aviao}')
    
    
else:
    pass

    
