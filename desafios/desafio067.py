multi = 0
n = int(input("qual o valor quer a tabuada: "))
while True: 
    while multi <= 10:
        res = n * multi
        print(f'O valor de {n} x {multi} = {res}')
        multi += 1
    n = int(input('\nquer mais algum numero?\nSe quiser parar coleque 0: '))
    if n != 0:
        multi = 0
    else:
        break
print('fim')
