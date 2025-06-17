from math import sqrt

catOposto = float(input('Digite o tamanho do cateto oposto: '))
catAdjacente = float(input('Digite o tamanho do cateto adjacente: ')) 

hipotenusa = sqrt(catOposto ** 2 + catAdjacente ** 2)

print("a hipotenusa é {:.2f}".format(hipotenusa))
