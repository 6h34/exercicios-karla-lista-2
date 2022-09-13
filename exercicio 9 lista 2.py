mat=[]
for i in range(0,5):
    l=[]
    mat.append(l)
    for j in range(0,5):
        mat[i].append(0)
tam=len(mat[0])-1
for k in range(0,len(mat[0])):
        mat[k][tam - k]=mat[k][tam - k]+1


for line in mat:
    print(tuple(line))
