par = []
impar = []
numeros = []

for c in range(7):
    num=int(input(f"Digite o {c+1} numero: "))
    numeros.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
        
print(numeros)
print(par)
print(impar)