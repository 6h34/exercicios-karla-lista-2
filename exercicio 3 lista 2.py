nome=str(input('insira um nome'))
cont=0
cont2=0
cont3=0
for p in nome:
    for letra in p:
        if letra.lower() in 'aeiou':
            cont+=1
        elif letra.lower() in ' ':
            cont2+=1
        else:
            cont3+=1
            

print('o numero de vogais nessa frase é de {}, o numero de espaços nessa frase é de {}, e o resto é de {}'.format(cont,cont2,cont3))

