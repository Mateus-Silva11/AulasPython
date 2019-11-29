#Dados informações
nome_c = input('Informe o nome da cerveja')
marca_c = input('Informe a marca da Cerveja')
tipo = input('Informe o tipo da Cerveja')
teor = int(input('Informe o teor alcolico'))
dicionario_cerveja = {'Nome':nome_c ,'Marca':marca_c , 'Tipo':tipo , 'Teor':teor }

#manipulando dado para adicionar no arquivo(Cervejaria.txt) metodo
def salvar_cerveja(dicionario_cerveja):
    arquivo = open('Aula_15/Cervejaria.txt','a')
    arquivo.write(f" {dicionario_cerveja['Nome']}; {dicionario_cerveja['Marca']}; {dicionario_cerveja['Tipo']} ; {dicionario_cerveja['Teor']} \n")
    arquivo.close()
#Impreção Metodo
def leitura():
    #criação da lista
    lista = []
    #abrindo o arquivo .txt em modo leitura ('R')
    arquivo = open('Aula_15/Cervejaria.txt', 'r')
    #criando um for para mostra todos os arquivos que estao no txt
    for linha in arquivo:   
        #linha.strinp() função utilizada para remove caracter da string exemplo \n
        linha = linha.strip()
        #linha.split() função utilizada para seprar a string de acordo com o caracter definido exemplo (';')
        lista_linha = linha.split(';')    
        #criando outro dicionario é adicionando a uma lista anteriormenete criada e atricuindo o valor dos dados
        dados ={'Nome': lista_linha[0] , 'Marca': lista_linha[1] , 'Tipo':lista_linha[2] , 'Teor': lista_linha[3]}
        #adicionando o dicionaria a lista
        lista.append(dados)
    #fechando o arquivo txt manualmente 
    arquivo.close()
    #retornando a lista com os dados do dicionario
    return lista
#Parte onde Salva no arquivo .txt
salvar_cerveja(dicionario_cerveja)
#Parte onde faiz a leitura dos dados do arquivo .txt
for d in leitura():
    print(f" Nome Cerveja:{d['Nome']} Marca: {d['Marca']} Tipo : {d['Tipo']} Teor: {d['Teor']}  ")