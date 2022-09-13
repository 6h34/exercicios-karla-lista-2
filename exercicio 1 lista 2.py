cel=0
far1=0
contc=0
contf=0
far=[]
far2=[]
for x in range(0,5):
    tem=int(input('insira uma temperatura em celsius'))
    cel+=tem
    contc+=1
    f=((9*cel)/5)+32
    far1+=f
    contf+=1
    far.append(f)
    
mediac=cel/contc 
mediaf=far1/contf

print('a media das temperaturas em celsius é ',mediac)
print('a media das temperaturas em farenheit é',mediaf)
print(far)
acimaf=0

for y in range(0,len(far)):
    if (far[y] > mediaf ) :
        acimaf+=1
        far2.append(far[y])

print('a temperatura em farenheit ficou acima da media {} vezes,{}'.format(acimaf,far2))
        




