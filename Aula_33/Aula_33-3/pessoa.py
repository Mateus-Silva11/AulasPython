class Pessoa:
    Id_pessoa = 0
    Nome = ''
    SobreNome = ''
    Idade = 0
    endereco_id = 0
    def exportar_txt(self,lista_pessoas):
    #----- Cria um arquivo e atribui a uma variável 'arquivo'
    with open('C:/Users/900148/Desktop/GitHub/AulasPython/Aula_33/Aula_33-3','w') as arquivo:
        #---- Percorre a lista de dicionário e salva no arquivo em formato pré-definido
        for p in lista_pessoas:
            pessoa_string = f'{str(p)}\n'
            arquivo.write(pessoa_string)
    
    def __str__(self):
        return f"{self.Id_pessoa};{self.Nome};{self.SobreNome};{self.Idade};{self.endereco_id}"