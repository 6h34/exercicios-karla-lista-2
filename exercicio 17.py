
contm=0
contf=0
contsim=0
contnao=0
cont_mas_nao=0

for x in range(0,2000):
    sexo=str(input('qual o seu sexo? m ou f?: ')).lower()
    resposta=str(input('gostou do nosso produto? s ou n?')).lower()
    if (sexo == 'm') and (resposta == 's'):
        contm+=1
        contsim+=1
    elif(sexo == 'm') and (resposta == 'n'):
        contm+=1
        contnao+=1
        cont_mas_nao+=1        
    elif(sexo == 'f') and (resposta == 's'):
        contf+=1
        contsim+1
    elif(sexo == 'f') and (resposta == 'n'):
        contf+=1
        contnao+=1
        print(sexo,resposta)
    

print('homens que votaram',contm)
print('mulheres que votaram',contf)

print('respostas positivas',contsim)
print('respostas negativas',contnao)
print('porcentagem de respostas masculinas negativas:',cont_mas_nao/contm*100,'%')
    
    
