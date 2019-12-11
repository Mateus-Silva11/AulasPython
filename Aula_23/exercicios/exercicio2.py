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
# 5) Crie um metodo salvar que pegue os seguintes dados do cliente e salve em um arquivo. 
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# 6) crie um metodo que possa atualizar os dados do cliente (código cliente (inteiro), 
# nome, idade (inteiro), sexo, email, telefone). Este metodo deverá alterar tambem o dado bruto para
# que na hora de salvar o dado num arquivo, o mesmo não estaja desatualizado.
class Cliente:

    def __init__ (self,dadobruto):
        self.dado_lista = dadobruto.split(';')
        self.codigo = None
        self.nome = None
        self.idade = None
        self.sexo = None
        self.email = None
        self.telefone = None
        self.atualizar(self.dado_lista[0],self.dado_lista[1],self.dado_lista[2],self.dado_lista[3],self.dado_lista[4],self.dado_lista[5])

    def imprimir(self):
        
        print(f'Codigo do Cliente: {self.codigo}')
        print(f'Nome do Cliente: {self.nome}')
        print(f'Idade do Cliente: {self.idade}')
        print(f'Sexo do Cliente: {self.sexo}')
        print(f'Email do clintde: {self.email}')
    
    def salvar(self):
        arquivo = open('Aula_23/sla.txt','a')
        arquivo.write(f"{self.codigo};{self.nome};{self.idade};{self.sexo};{self.email};`{self.telefone}")
        arquivo.close()

    def atualizar(self,codigo,nome,idade,sexo,email,telefone):
        self.codigo = int(codigo)
        self.nome = nome
        self.idade = int(idade)
        self.sexo = sexo 
        self.email = email
        self.telefone = telefone
        self.dado_lista = f'{codigo};{nome};{idade};{sexo};{email};{telefone}\n'


# 6) crie um metodo que possa atualizar os dados do cliente (código cliente (inteiro), 
# nome, idade (inteiro), sexo, email, telefone). Este metodo deverá alterar tambem o dado bruto para
# que na hora de salvar o dado num arquivo, o mesmo não estaja desatualizado.

cliente = Cliente('1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117')
cliente.imprimir()
cliente.atualizar(1,'Matues',123,'m','fsfds@gmail.com','2324233424')
cliente.salvar()
