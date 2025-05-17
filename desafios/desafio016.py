from math import trunc

numeroReal = float(input('Escreva um numero real: '))

print("O numero real que escolheu foi: {} e a parte inteira desse numero é {}".format(numeroReal, trunc(numeroReal)))

print("O numero real que escolheu foi: {} e a parte inteira desse numero é {:.0f}".format(numeroReal, numeroReal))