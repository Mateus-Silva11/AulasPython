class Squad:
    def __init__(self):
        self.idSquad = 0
        self.Nome = ''
        self.Descricao = ''
        self.NumeroPessoas = 0
        self.LinguagemBackEnd = ''
        self.FrameworkFrontEnd = ''

    def __str__(self):
        return f'{self.idSquad};{self.Nome};{self.Descricao};{self.NumeroPessoa};{self.LinguagemBackEnd};{self.FrameworkFronteEnde};'