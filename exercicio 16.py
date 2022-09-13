nome=[]
altura=[]

n=str(input('insira o nome da participante: '))
while n != 'fim':
    nome.append(n)
    al=float(input('insira a altura da participante'))
    altura.append(al)
    n=str(input('insira o nome da participante: '))
    if n == 'Maria' or 'maria':
        nome.append(n)
        al=float(input('insira a altura da participante'))
        altura.append(al)
        break



print(nome,altura)
maiornome=[]
maioraltura=0

for x in range(0,len(altura) and len(nome)):
    for y in range(0,len(altura)and len(nome)):
        if altura[x] > altura[y] 
            maioraltura=maioraltura+altura[x]
            maiornome.append(nome[x])
        
    
      
        else:
            pass
print(maiornome,maioraltura)
        
