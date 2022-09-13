vetor1=[]
vetor2=[]
for x in range(0,16):
    vetor=int(input('insira um valor: '))
    vetor1.append(vetor)
    vetor2.append(vetor)

for y in range(0,8):
    aux=vetor1[y]
    vetor1[y]=vetor1[y+8]
    vetor1[y+8]=aux

print(vetor1)
print(vetor2)
