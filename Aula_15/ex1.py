a = input('Informe seu nome')

arquivo = open('teste2.txt','a')
arquivo.write( a + '\n')
a.close()
