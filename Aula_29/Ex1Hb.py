# A HBSIS Airlines é uma empresa de aviação que opera rotas internacionais a partir de Blumenau.
# Cada voo é tripulado por seis elementos, sendo que estes se dividem em dois grupos: a tripulação
# técnica e a tripulação de cabine. A tripulação técnica é constituída pelo piloto e dois oficiais. 
# A tripulação de cabine é constituída pelo chefe de serviço de voo e duas comissárias.
# O transporte dos tripulantes entre o terminal e o avião é efetuado através de um Smart Fortwo, que
# é um veículo que leva apenas duas pessoas. Por política da empresa, apenas o piloto e o chefe de
# serviço de voo podem dirigir este veículo. É também política da empresa que nenhum dos oficiais
# pode ficar sozinho com o chefe de serviço de bordo, e nem nenhuma das comissárias pode ficar
# sozinha com o piloto.  No terminal de embarque estão os seis tripulantes e ainda um policial 
# junto com um presidiário. Estes oito elementos terão que embarcar segundo as regras descritas acima. 
# A empresa não coloca nenhum limite para o número de viagens entre o terminal e o avião.

# Por motivos de segurança o presidiário não pode ficar sozinho em momento algum com os
# tripulantes sem a presença do policial, nem no terminal e nem no avião. De forma a facilitar o
# processo, a empresa autorizou que o policial pudesse dirigir o veículo também.


# Meu resumo

# Cada voo tem seis elementos.
# seis elementos formam dois grupos sendo eles:

# 1º A Tripulação Técnica segintes elementos:
# 1) Piloto
# 2) Dois Oficiais

# 2º A Tripulação cabine 
# 1) Chefe de serviço de voo 
# 2) Duas Comissárias

# O transporte dos tripulantes entre o terminal e o avião é efetuado através de um Smart Fortwo, que um veiculo que eleva apenas duas pessaos

# Politica da emprese somente o piloto e o chefe de serviço 

# No terminal de embarque tem seis tripulantes e ainda um policial junto com presidiário 

# Esse Oito elemtos tem que segui as regras acima


# Requisitos:
# 1 - Sempre que o Fortwo se mover, apresentar no console quando ele chega no destino
# 2 - Sempre que acontecer um embarque, apresentar quais elementos estão embarcando
# 3 - Sempre que acontecer um embarque no terminal, apresentar quem está no terminal
# 4 - Sempre que acontecer um embarque no avião, apresentar quem está no avião
# 5 - Deve ser feito em Python


#Por política da empresa, apenas o piloto e o chefe de
# serviço de voo podem dirigir este veículo. É também política da empresa que nenhum dos oficiais
# pode ficar sozinho com o chefe de serviço de bordo, e nem nenhuma das comissárias pode ficar
# sozinha com o piloto.  No terminal de embarque estão os seis tripulantes e ainda um policial 
# junto com um presidiário.


Piloto = input('Informe Quem vai pilotar o aviao 1) Piloto 2) Chefe de Serviço 3) Policia')

if Piloto == '1':
    print('Quem devera embarcar Primeiro com o Piloto devera ser o Chefe de serviço')

elif Piloto == '2':
    print('Quem devera embarcar Primeiro com o Chefe devera ser o Piloto')
else:
    pass