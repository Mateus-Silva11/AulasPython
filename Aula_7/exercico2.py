#Exercicio 2 - Dicionario
# Escreva um programa que leia os dados de 11 jogadores
# Jogador : Nome, Posicao, Numero, PernaBoa 
# Crue um dicionario para armazenar os dados
# Imprima todos os jagadores e seus dados

lista_jogadores = []

for j in range(1,12):   
    jogador = {'Nome':'' , 'Posicao': '' , 'Numero': '', 'PernaBoa':''}
    jogador['Nome']= input(f'Informe o Nome do {j}º Jagador')
    jogador['Posicao'] = input('Informe a posição que o Jogador joga')
    jogador['Numero'] = input('Informe o Numero do Jogador')
    jogador['PernaBoa'] = input('Informe a PernaBoa do Jogador')
    lista_jogadores.append(jogador)

for x in lista_jogadores:
    
    print(f'Dados do Jogador{x}')
    