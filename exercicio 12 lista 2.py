def pi(x,y):
    a=x**2
    print(a)
    b=y**2
    print(b)
    c=a+b
    print(c)
    if c <= 4:
        d=10**6
        print(d)
        e=c/d
        return e
    else:
        print('x+y é maior que 4')
        return False


import random

l=[0,1,2]

n1=random.choice(l)
n2=random.choice(l)

resultado=pi(n1,n2)
print(resultado)

