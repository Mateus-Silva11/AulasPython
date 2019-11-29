from faixa import criar_faixa , salvar_faixa

musica = input('digite uma musica')
artista = input('digite o nome do artiste')
album = input('digite o nome do album')

faixa = criar_faixa(musica,artista,album)
salvar_faixa(faixa)

print(f'Faixa criada: {faixa} ')


