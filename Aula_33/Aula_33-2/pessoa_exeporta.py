def exportar_txt(lista_pessoas):
    #----- Cria um arquivo e atribui a uma variável 'arquivo'
    with open('Aula_33/pessoas2.txt','a') as arquivo:
        #---- Percorre a lista de dicionário e salva no arquivo em formato pré-definido
        for p in lista_pessoas:
            arquivo.write(f"{p['Id_pessoa']};{p['Nome']};{p['SobreNome']};{p['Idade']};{p['endereco_id']}\n")