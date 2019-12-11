# Aula 22 - 10-12-2019
# Como Tratar e Trabalhar Erros!!!

# Com base no seguinte dado bruto:

dadobruto = '1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117'

# 1) Faça uma classe cliente que receba como parametro o dado bruto.
# 2) A classe deve iniciar (__init__) guardando o dado bruto nume variável chamada self.dado_bruto
# 3) As variáveis  código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# devem iniciar com o valor None
# 4) Crie um metodo que pegue o valor bruto e adicione nas variáveis:
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# convertendo os valores de string para inteiros quando necessários. 
# (Faça da forma que vocês conseguirem! O importante é o resultado e não como chegaram nele!)

class Cliente:

    def __init__ (self,dadobruto):
        self.dado_lista = dadobruto.split(';')
        self.codigo = None
        self.nome = None
        self.idade = None
        self.sexo = None
        self.email = None
        self.telefone = None
        self.codigo = self.dado_lista[0]
        self.nome = self.dado_lista[1]
        self.idade = self.dado_lista[2]
        self.sexo = self.dado_lista[3]
        self.email = self.dado_lista[4]
        self.telefone = self.dado_lista[5]

    def imprimir(self):
        
        print(f'Codigo do Cliente: {self.codigo}')
        print(f'Nome do Cliente: {self.nome}')
        print(f'Idade do Cliente: {self.idade}')
        print(f'Sexo do Cliente: {self.sexo}')
        print(f'Email do clintde: {self.email}')

cliente = Cliente('1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117')
cliente.imprimir()
