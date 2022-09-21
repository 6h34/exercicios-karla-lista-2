def somarMatrizes(matriz1, matriz2):
   
    if(len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0])):
        return print('nao é possivel fazer a soma das matrizes, pois seus valores sao diferentes!')
    result = []
    for i in range(len(matriz1)):   
        result.append([])
        for j in range(len(matriz1[0])):
            result[i].append(matriz1[i][j] + matriz2[i][j])
    return result

def multiplica(matriz,mult):
    result = []
    for i in range(len(matriz)):
        result.append([])
        for j in range(len(matriz)):
            result[i].append(matriz[i][j] * mult)
    return result
        
    

m1=[[1,2],[3,4]]
m2=[[2,3],[4,5]]
resultado=somarMatrizes(m1,m2)
print(resultado)

m=2
resultado2=multiplica(m2,m)
print(resultado2)
