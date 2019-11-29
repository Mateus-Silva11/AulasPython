def criar_faixa(musica,artista,album):
    faixa = {'Musica':musica ,'Artista':artista , 'Album':album }
    return faixa

def salvar_faixa(faixa):
    arquivo = open('Aula_16/faixas.txt','a')
    arquivo.write(f"{faixa['Musica']};{faixa['Artista']};{faixa['Album']}")
    arquivo.close()