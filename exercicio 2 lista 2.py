v=[]
z=[]
cont=0
for a in range(0,5):
    v.append(int(input('elemento:')))
    print(v)
    
for x in range(0,5):
    if v[x] % 2 == 0:
        cont+=1
        z.append(v[x])
        
        print(v[x])


print('o numero de numeros positivos nesse vetor sao: {}'.format(cont))
print(z)


