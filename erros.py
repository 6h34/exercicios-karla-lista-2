def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('erro, digite um valor válido!!!')
            continue
        except (KeyboardInterrupt):
            print('erro, nao foi digitado nenhum valor!!!')
            continue
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('erro, digite um valor válido!!!')
            continue
        except(KeyboardInterrupt):
            print('erro, nao foi digitado nenhum valor')
            continue
        else:
            return n

num=leiaint('digite um valor: ')
num2=leiafloat('digite um numero decimal: ')



print(f'O valor digitado foi {num}, o valor decimal digitado foi: {num2}')
