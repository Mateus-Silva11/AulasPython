from faixa import criar_faixa , salvar_faixa , ler_faixa

for linha in range(1,3):

    print('+'*50)
    print('\n')
    musica = input('digite uma musica')
    artista = input('digite o nome do artiste')
    album = input('digite o nome do album')                     
    print('\n')
    print('+'*50)
    
    
    faixa = criar_faixa(musica,artista,album)
    salvar_faixa(faixa)
    ler = ler_faixa()

for linha in ler:
    print(f" {linha}° faixa : Nome da Musica: {linha['Musica']} - Nome do Artista: {linha['Artista']} - Nome do Album {linha['Album']} ")
