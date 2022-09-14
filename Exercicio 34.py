alunoslista = []
alunosacimamedia = []
idadelista = []
notalista= []
soma = 0
infocompleta = []

quantidadealunos = int(input('A quantidade de alunos: '))

for i in range(0,quantidadealunos):
    nome = str(input('O nome do aluno: '))
    nota = float(input('A nota do aluno: '))
    soma += nota
    idade = int(input('A idade do aluno: '))
    alunoslista.append(nome)
    notalista.append(nota)
    idadelista.append(idade)
    infocompleta.append

media = soma/quantidadealunos

#print(alunoslista)
#print(notalista)
#print(idadelista)

print(f'A média das notas finais dos alunos foi {round(media)}!')

for i in range(0, len(notalista)):
    if notalista[i] > media:
        alunosacimamedia.append(alunoslista[i])

print(f'Os alunos acima da média foram {alunosacimamedia}!')



for i in range(0, (len(notalista))-1):
    for j in range(i+1, len(notalista)):
        if notalista[i] > notalista[j]:
            aux1 = alunoslista[i]
            aux2 = idadelista[i]
            aux3 = notalista[i]

            alunoslista[i] = alunoslista[j]
            idadelista[i] = idadelista[j]
            notalista[i] = notalista[j]


            alunoslista[j] = aux1
            idadelista[j] = aux2
            notalista[j] = aux3



#print(alunoslista)
#print(notalista)
#print(idadelista)

for i in range(0,quantidadealunos):
    aux4 = str(notalista[i])
    aux5 = str(idadelista[i])
    vetaux = [alunoslista[i]+' '+'Idade:'+' '+aux5+' '+'Nota:'+' '+aux4] 
    infocompleta.append(vetaux)

print(infocompleta[::-1])

invertida = infocompleta[::-1]

for line in invertida:
    print(line[::-1])