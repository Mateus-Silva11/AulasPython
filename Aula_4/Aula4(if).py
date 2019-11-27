idade = 17.5
# If simples, validação de apenas uma condição
if idade == 18:
    print('Maior')
# if com else, caso a condicão validada pelo if não seja verdadeira, o else é executado
if idade < 18:
    print('Menor') 
else:
    print('Maior')
# if com ELIF e else Caso a condição do validada no if seja falsa é validado a condição do ELIF caso a condição do elif seja falsa else é executado          
if idade < 18:
    print('Menor') 
elif idade==18:
    print('sla')
else:
    print('Maior')
#if com variavel booleana em caso de variavel booleana, não é necessario a validação(==True) Pois o If ja valida o se o conteúdo da variável é True, senão vai para o Else    
