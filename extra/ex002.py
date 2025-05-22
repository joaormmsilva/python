idade = int(input('Escreva sua idade: '))

if idade >= 5 and idade <7:
    print('Você é um atleta Infantil')
elif idade >= 8 and idade <=10:
    print('Você é um atleta Iniciante')
elif idade >= 11 and idade <=14:
    print('Você é eum atleta Juvenil')
elif idade >= 15 and idade <= 17:
    print('Você é um atleta Junior')
elif idade > 17:
    print('Você é um atleta Sénior')
else:
    print('Você ainda não tem idade para ser considerado um atleta')