# Crie uma classe cliente:

# 1) deve ter como atributos: codigo, cpf, nome, idade, sexo

# 2) como metodos: receber salario, comprar, pagar divida

# Quando recebe aumenta o dinheiro na carteira.

# quando compra aumenta os bens e diminui o dinheiro na carteira

# Se comprar e não tiver dinheiro o suficiente deve diminuir o dinheiro da carteira
# e aumentar a divida.

# Para pagar a divida tem que ter dinheiro o suficiente na carteira

# 3) atributos de estado: dinheiro na carteira, divida, bens

class Cliente:

    def __init__(self, codigo,cpf,nome,idade,sexo):
        self.codigo = codigo
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        
        self.salario = 0.0
        self.bens = []
        self.divida = 0.0
        self.carteira = 0 

    def set_salario(self,salario):
        self.salario= salario
        self.carteira += salario
        return salario
    
    def comprar(self,bem,preco):
        if self.carteira - preco < 0:
            self.divida -= self.carteira - preco
            self.carteira = 0
            
        else:
            self.bens.append(bem)
            self.carteira -= preco
        
    def pagar(self,pagar):
        self.divida += pagar

cliente = Cliente(1,'123.232.233-32','Mateus',18,'m')
cliente.set_salario(25446)
cliente.set_salario(25446)
cliente.comprar('Casa', 1000.00)
cliente.comprar('Carro', 1000.00)

print(f'Nome do cliente {cliente.nome}')
print(f'Idade do Cliente: {cliente.idade}')
print(f'Cpf do Cliente : {cliente.cpf}')
print(f'Sexo do Cliente: {cliente.sexo}')
print(f'Codigo do cliente : {cliente.codigo}')
print(f'Carteira do clinte {cliente.carteira}')
print(f'Divida cliente é de : {cliente.divida}')
print(f'bens do cliente {cliente.}')