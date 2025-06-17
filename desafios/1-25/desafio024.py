cidade = input("digite o nome da sua cidade: ")

if cidade[:5] != 'santo':
    print("A sua cidade se chama {}".format(cidade))
elif cidade[:5] == 'santo':
    print("A sua cidade tem nome de santo e seu numero é {}".format(cidade))
    
