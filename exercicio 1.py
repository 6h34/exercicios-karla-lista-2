def mat_mul(A,B):
    num_linhas_A, num_colunas_A = len(A),len(A[0])
    num_linhas_B, num_colunas_B = len(B),len(B[0])
    c=[]
    if num_colunas_A == num_colunas_B:
        for linha in range(num_linhas_A):
            c.append([])
            for coluna in range(num_colunas_B):
                c[linha].append(0)
                for k in range(num_colunas_A):
                    c[linha][coluna] += A[linha][k] * B[k][coluna]
                    return c
    else:
        print('Erro, Matriz com tamanho diferente!')
        return c
        

    

v=[]
l=int(input('insira o numero de linhas'))
c=int(input('insira o numero de colunas'))

for x in range(0,l):
    v.append([])
    for y in range(0,c):
        v[x].append(int(input('insira um valor')))



v2=[]
l2=int(input('insira o numero de linhas'))
c2=int(input('insira o numero de colunas'))

for a in range(0,l2):
    v2.append([])
    for b in range(0,c2):
        v2[a].append(int(input('insira um valor')))

resultado=mat_mul(v,v2)
print(resultado)
                 
    
