def criar_faixa(musica,artista,album):
    faixa = {'Musica':musica ,'Artista':artista , 'Album':album }
    return faixa

def salvar_faixa(faixa):
    arquivo = open('Aula_16/faixas.txt','a')
    arquivo.write(f"{faixa['Musica']};{faixa['Artista']};{faixa['Album']}\n")
    arquivo.close()

def ler_faixa():
    arquivo = open('Aula_16/faixas.txt','r')
    lista = []
    for linha in arquivo:
        linha = linha.strip()
        dedados_faixa = linha.split(';')
        faixa = criar_faixa(dedados_faixa[0], dedados_faixa[1], dedados_faixa[2])
        lista.append(faixa)
    arquivo.close()    
    return lista    
