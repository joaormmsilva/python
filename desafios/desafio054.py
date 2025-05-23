pesos=[]
for c in range(5):
    peso = int(input("fale seu peço "))
    pesos.append(peso)
 
pesos.sort()
print('o maior peso é {} e o menor peso é {}'.format(pesos[0],pesos[-1]))