# Banco de Dados
#SGBD - Sistema Gereciador de Banco de Dados
# Mysql , SqlServer ...
# Mysql '=MariaDb

#CRUD
# C= CREATE
# R= READ
# U= UPDATE
# D= DELETE

#Pip3 install flask_mysql

import MySQLdb

print('-'*50)
conexao = MySQLdb.connect(host='localhost',database='aula_bd',user='root',passwd='' )
cursor = conexao.cursor()
cursor.execute('SELECT * FROM tb_pessoa')
pessoas = cursor.fetchall()
for p in pessoas:
    print(p)

print('-'*50)
