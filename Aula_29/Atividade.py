
fortwo = []
embarcados = []
terminal = ['piloto','official1','official2','comissaria1','comissaria2','chefe','policial','preso']
hsaida = ''
hchegada = ''
hora = {'Hs':hsaida ,'Hc':hchegada}
print('Tripulação completa = Piloto, Chefe de serviço de bordo, 2 comissárias , 1 policial e 1 preso, 2 oficiais')

print('Etinerário:\n 1 viagem - piloto + oficial \n2 viagem - piloto + oficial \n 3 viagem - chefe + comissaria \n 4 viagem - chefe + piloto \n 5 viagem -chefe + comissaria \n 6 viagem - policia + preso \n 7 viagem - chefe + piloto ')
proc = input ('Deseja iniciar ? s/n ')
while proc == 's':

    opcao = input('qual viagem voce gostaria de consultar? ')
    if opcao == '1':
        hsaida = input('informe o horario de saida')
        hchegada = input('informe o horario de chegada')
        hora = {'Hs':hsaida ,'Hc':hchegada}
        terminal.remove('official1')
        terminal.remove('piloto')
        terminal.append('Chefe')
        terminal.append('Comissaria1')
        terminal.append('Comissaria2')
        terminal.append('Policial')
        terminal.append('Ladrão')
        fortwo.append('piloto') 
        fortwo.append('official1')
        print(f'Pessoas no fortwo neste momento: {fortwo[0]} e {fortwo[1]}')
        embarcados.append('official1')
        fortwo.remove('official1')
        print(f'pessoas no avião {embarcados}')

    elif opcao == '2':
        hsaida = input('informe o horario de saida')
        hchegada = input('informe o horario de chegada')
        hora = {'Hs':hsaida ,'Hc':hchegada}
        terminal.remove('official2')
        terminal.append('Chefe')
        terminal.append('Comissaria1')
        terminal.append('Comissaria2')
        terminal.append('Policial')
        terminal.append('Ladrão')
        
        fortwo.append('official2')
        fortwo.append('piloto')
        print(f'Pessoas que passaram pelo fortwo neste momento: {fortwo[0]} e {fortwo[1]}')
        embarcados.append('official2')
        fortwo.remove('official2')
        print(f'pessoas no avião {embarcados}')

    elif opcao == '3':
        hsaida = input('informe o horario de saida')
        hchegada = input('informe o horario de chegada')
        hora = {'Hs':hsaida ,'Hc':hchegada}
        terminal.remove('chefe')
        terminal.remove('comissaria1')
        terminal.append('piloto')
        
        
        
        terminal.append('Comissaria2')
        terminal.append('Policial')
        terminal.append('Ladrão')



        fortwo.append('chefe')
        fortwo.append('comissaria1')
        print(f'Pessoas no fortwo neste momento: {fortwo[0]} e {fortwo[1]}')
        embarcados.append('comissaria1')
        fortwo.remove('comissaria1')
        print(f'pessoas no avião {embarcados}')
        
    elif opcao == '4':
        hsaida = input('informe o horario de saida')
        hchegada = input('informe o horario de chegada')
        hora = {'Hs':hsaida ,'Hc':hchegada}
        terminal.remove('piloto')

        
        terminal.append('Policial')
        terminal.append('Ladrao')


        fortwo.append('piloto')
        fortwo.append('chefe')
        print(f'Pessoas no fortwo neste momento: {fortwo[0]} e {fortwo[1]}')
        embarcados.append('piloto')
        fortwo.remove('piloto')
        print(f'pessoas no avião {embarcados}')

    elif opcao == '5':
        hsaida = input('informe o horario de saida')
        hchegada = input('informe o horario de chegada')
        hora = {'Hs':hsaida ,'Hc':hchegada}
        terminal.remove('comissaria2')
        
        terminal.append('piloto')
        terminal.append('policial')
        terminal.append('Ladrao')

        fortwo.append('chefe')
        fortwo.append('comissaria2')
        print(f'Pessoas no fortwo neste momento: {fortwo[0]} e {fortwo[1]}')
        embarcados.append('comissaria2')
        fortwo.remove('comissaria2')
        print(f'pessoas no avião {embarcados}')


    elif opcao == '6':
        hsaida = input('informe o horario de saida')
        hchegada = input('informe o horario de chegada')
        hora = {'Hs':hsaida ,'Hc':hchegada}
        terminal.append(piloto)
        terminal.remove('policial')
        terminal.remove('ladrao')

        terminal.append('chefe')
        terminal.append('Policial')
        terminal.append('Ladrão')

        fortwo.append('policial')
        fortwo.append('ladrao')
        print(f'Pessoas no fortwo neste momento: {fortwo[0]} e {fortwo[1]}')
        embarcados.append('ladrao')
        embarcados.append('policial')
        fortwo.remove('ladrao')
        fortwo.remove('policial')
        fortwo.append('chefe')
        print(f'pessoas no avião {embarcados}')

    elif opcao == '7':
        hsaida = input('informe o horario de saida')
        hchegada = input('informe o horario de chegada')
        hora = {'Hs':hsaida ,'Hc':hchegada}
        terminal.remove('piloto')
        print('Terminal vazio')
        fortwo.append('chefe')
        fortwo.append('piloto')
        print(f'Pessoas no fortwo neste momento: {fortwo[0]} e {fortwo[1]}')
        embarcados.append('chefe')
        embarcados.append('piloto')
        fortwo.remove('chefe')
        fortwo.remove('piloto')
        print(f'pessoas no avião {embarcados}')
    else:
            print('Viagem inexistente')
    proc = input ('Deseja iniciar ? s/n')
    