def palindromo(x):
    vetor=[]
    vetor2=[]
    palavra=x
    vetor.append(palavra)
    palavra2=palavra[::-1]
    vetor2.append(palavra2)
    if vetor == vetor2:
        return True
    else:
        return False


print('Descobrindo se uma palavra é um palíndromo')
a=str(input('insira uma plaavra:'))
resultado=palindromo(a)
print(resultado)


    
