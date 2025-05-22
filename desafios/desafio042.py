r1 = float(input("qual o valor da primeira reta: "))
r2 = float(input("qual o valor da segunda reta: "))
r3 = float(input("qual o valor da terceira reta: "))


if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1 :
    if r1 == r2 == r3:
        print('É um triângulo EQUILÁTERO.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('É um triângulo ISÓSCELES.')
    else:
        print('É um triângulo ESCALENO.')
else:
    print('❌ As retas NÃO PODEM formar um triângulo.')