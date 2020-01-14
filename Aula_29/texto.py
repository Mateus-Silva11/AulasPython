embarque = ['Piloto', 'Chefe de serviço','Policial','Oficial1','Oficial2','Comissaria1','Comissaria2','Presidiario']
def txt_terminal (embarque):
    lista = []
    dados = ','.join(embarque) # Convertendo uma lista em String e atribuindo ela a variável dados
    arquivo = open('Aula_29/lista_terminal.txt', 'w') # Criando arquivo
    arquivo.write(dados)  # Inserindo conteúdo no arquivo
    lista.append(dados) # Inserindo na lista os dados do arquivo
    arquivo.close() # Fehando arquivo
    return lista
def txt_aviao():
    dados = ','.join(aviao)       
    arquivo = open('Aula_29/lista_aviao.txt', 'w') # Criando arquivo
    arquivo.write(dados)  # Inserindo conteúdo no arquivo
    arquivo.close() # Fehando arquivo