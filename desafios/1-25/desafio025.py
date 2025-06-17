nome = str(input("digite o seu numero completo: "))
verificar = nome.lower().find('silva')

if verificar != -1:
    print("O seu nome é {} e ele tem Silva no meio ".format(nome))
elif verificar == -1:
    print("O seu nome é {}".format(nome))
    


