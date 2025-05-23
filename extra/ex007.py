email = input('digit seu email: ')

if email.find('@') != -1 and email.endswith('.com') == True:
    print('o seu email tem @ e termina com .com')
elif email.find('@') == -1 and email.endswith('.com') == False:
    print('isso não é um email')
elif email.find('@') == -1:
    print('seu email falta @')
elif email.endswith('.com') == False:
    print('o ".com" não existe ou esta fora final')
