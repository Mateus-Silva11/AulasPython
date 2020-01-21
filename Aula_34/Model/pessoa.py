class Pessoa:
    Id_pessoa= 0
    Nome = ''
    SobreNome = ''
    Idade = 0
    endereco_id = 0
    
    def __str__(self):
        return f"{self.Id_pessoa};{self.Nome};{self.SobreNome};{self.Idade};{self.endereco_id}"