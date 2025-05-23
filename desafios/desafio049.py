num = int(input("Escolha um numero para que seja mostrada a sua tabuada"))

for c in range(0,11):
    x = num * c
    print('x{} = {}'.format(c,x))