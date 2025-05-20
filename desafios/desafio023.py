numero = int(input("Escreva um numero de 0 ate 9999: "))

if numero <0 or numero > 9999:
    print("Numero invalido")
else:
    numero_str = str(numero)
    tamanho = len(numero_str)
    
    if tamanho == 1:
        print("o numero ditado foi {}".format(numero))
        print("Unidade {}".format(numero_str[0]))
    elif tamanho == 2:
        print("o numero ditado foi {}".format(numero))
        print("Unidade {}".format(numero_str[0]))
        print("Dezena {}".format(numero_str[1]))
    elif tamanho == 3:
        print("o numero ditado foi {}".format(numero))
        print("Unidade {}".format(numero_str[0]))
        print("Dezena {}".format(numero_str[1]))
        print("Centena {}".format(numero_str[2]))
    elif tamanho == 4:
        print("o numero ditado foi {}".format(numero))
        print("Unidade {}".format(numero_str[0]))
        print("Dezena {}".format(numero_str[1]))
        print("Centena {}".format(numero_str[2]))
        print("Milhar {}".format(numero_str[3]))
