class Endereco:
    Id_endereco = 0
    Rua = ''
    cep = ''
    bairro = ''
     
    def __str__(self):
        return f"{self.Id_endereco};{self.Rua};{self.cep};{self.bairro}"
        