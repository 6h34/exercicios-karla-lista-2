def maior_que_10(matriz):
    cont=0
    for x in range(0,len(matriz)):
        for y in range(0,len(matriz)):
            if matriz[x][y] > 10:
                cont+=1

    return cont

c=[]
for a in range(0,4):
    l=[]
    c.append(l)
    for b in range(0,4):
        c[a].append(int(input('insira o elemento')))

resultado=maior_que_10(c)
print('o numero de valores maiores que 10 na matriz sao:',resultado)
               
