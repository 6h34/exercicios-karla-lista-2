v=[4,6,5,8,1,7,3,0,2]
k=[4,1,6,3,8,2,5,7,0]
t=[4,6,5,8,1,7,3,0,2]
for i in range(0,len(v)):
    if v[i] != k[i]:
        v[i]=k[i]
        print(v)
    else:
        pass

print('vetor ordenado corretamente',v)
print('vetor original',t)



