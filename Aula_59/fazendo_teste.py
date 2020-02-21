#---- Rev Classe
#---- Métodos de Classe
#---- Método __init__
#---- Variáveis de classe
#---- Variáveis privadas
#---- Metodos Getters e Setters

class Calc:
    def __init__(self, numero1,numero2):
        # Variável de classe
        self.__n1 = numero1
        self.__n2 = numero2
        self.__resultado = 0

    def set_n1(self, valor):
        self.__n1 = valor
    def get_n1(self):
        return self.__n1

    def set_n2(self, valor):
        self.__n2 = valor
    def get_n2(self):
        return self.__n2

    def get_resultado(self):
        return self.__resultado

    def soma(self):
        a = self.__resultado = self.__n1 + self.__n2
        return a

    def multiplicacao(self):
        a = self.__resultado = self.__n1 * self.__n2
        return a

    def subtracao(self):
        self.__resultado = self.__n1 - self.__n2
        return self.__resultado

c = Calc(10,20)
assert isinstance(c, Calc)
for i in range(1000):
    c.set_n1(i)
    assert c.get_n1() == i
    c.set_n2(i)
    assert c.get_n2() == i
c.set_n1(50)
c.set_n2(20)
assert c.soma() == 70
assert c.subtracao() == 30
assert c.multiplicacao() == 1000
assert c.soma() == c.get_resultado()
assert c.subtracao() == c.get_resultado()
assert c.multiplicacao() == c.get_resultado()

# Instanciando um objeto da classe Calc
#c = Calc(10,20)
#print(c.get_n1())
#print(c.get_n2())
#c.set_n1(50)
#c.set_n2(100)
#print(c.get_n1())
#print(c.get_n2())
#print(c.get_resultado())