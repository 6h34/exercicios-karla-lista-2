m=[]
pessoa=[]
idade=[]
nota=[]
pessoas_acima_media=[]
notas=0
cont=0
mdecrescente=[]
m2=[]
for i in range(5):
    linha= []
    p=input('insira o nome: ')
    z=int(input('insira a idade'))
    linha.append(p)
    linha.append(z)
    pessoa.append(p)
    idade.append(z)
    nota1=int(input('insira a nota'))
    nota.append(nota1)
    notas+=nota1
    cont+=1
    linha.append(nota1)
    m.append(linha)
    

for k in range(len(m)):
    if m[k][2] >= 7:        
        pessoas_acima_media.append(m[i][0])

for i in range(len(nota)):
    for j in range(len(nota)):
        if nota[i]>=nota[j]:
            temp=nota[i]
            nota[i]=nota[j]
            nota[j]=temp
            temp1=pessoa[i]
            pessoa[i]=pessoa[j]
            pessoa[j]=temp1
            temp2=idade[i]
            idade[i]=idade[j]
            idade[j]=temp2
       

media=notas/cont


print(media)

print(pessoas_acima_media)
print(pessoa)
print(idade)
print(nota)
    



    


        
