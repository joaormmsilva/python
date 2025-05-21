ano = int(input("Qual o seu ano: "))


if ano % 4 == 0 and ano % 400 == 0 or ano % 100 != 0:
    print("o ano é bixesto") 
else:
    print("não é bisexto")