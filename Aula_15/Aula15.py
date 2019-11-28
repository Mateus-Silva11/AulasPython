# Aula 15 
# Manipulação de arquivos

arquivo = open('teste.txt','a')
arquivo.write('Mateus Aula15\n')
arquivo.close()

#Leitura

arquivo = open('teste.txt','r')
for linha in arquivo:
    print(linha)
arquivo.close()
