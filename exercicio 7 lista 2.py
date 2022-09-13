def anagrama(frase1,frase2):
    resultado= False
    frase1_ordenada=sorted(frase1)
    frase2_ordenada=sorted(frase2)
    if frase1_ordenada == frase2_ordenada:
        resultado=True
        print('é um anagrama')
    else:
        print('nao é um anagrama')
    return resultado

a=str(input('insira uma palavra ou frase ')).strip().lower()
b=str(input('insira uma palavra ou frase ')).strip().lower()
c=anagrama(a,b)
print(c)
    
