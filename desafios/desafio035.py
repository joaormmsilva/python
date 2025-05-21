r1 = float(input("qual o valor da primeira reta: "))
r2 = float(input("qual o valor da segunda reta: "))
r3 = float(input("qual o valor da terceira reta: "))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1 :
    print("ok")
else:
    print("não")