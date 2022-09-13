vetor=[]
cont=0
print('descobrir quantas vezes o numero x se repete no vetor!!!')
for x in range(0,30):
    vetor.append(int(input('insira o valor do vetor')))

c=int(input('insira o valor a ser descoberto: '))

for y in range(0,len(vetor)):
    if vetor[y] == c:
        cont+=1
  



print('o valor se repete {} vezes'.format(cont))
