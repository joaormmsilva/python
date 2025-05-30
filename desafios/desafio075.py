cont = 0
pares = []
par = 0
trez = 0
nove = 0
numeros = []
while cont < 4:
    numero = int(input("Digite o valor: "))
    numeros.append(numero)
    if numero == 9:
        nove +=1
    if numero % 2 == 0:
        pares.append(numero)
        par +=1
    if numero == 3:
        tres = numeros.index(3)
        trez += 1
    cont += 1
    
if nove != 0:
    print(f'Voce digitou {nove} vez o numero nove')
else:
    print('Voce não colocou numero 9')


if trez != 0:
    print(f'Voce digitou o numero 3 e ele foi o seu {tres+1} numero digitado')
else:
    print('Voce não digitou nenhum numero 3')
    
if par != 0:
    print(f'Dentro dos 4 numeros digitados {par} par')
else:
    print('todos numeros digitados são impares')