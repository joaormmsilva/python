s = 0
numeros = []
cont = 0

while True:
    n = int(input('Digite um numero [para parar coloque 0] '))
    if n == 0:
        break
    numeros.append(n)
    s += n
    cont += 1
    
print(f'Os numeros colados são {numeros} o tatal de numero foram {cont} e a soma de todos eles dara {s}')