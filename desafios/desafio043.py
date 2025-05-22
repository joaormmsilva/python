altura = float(input('digite sua altura: '))
peso = float(input('digite seu peso: '))
imc = peso / (altura ** 2) 

if imc < 18.5:
    print('🔸 Você está ABAIXO DO PESO.')
elif imc < 25:
    print('✅ Você está com PESO IDEAL.')
elif imc < 30:
    print('⚠️ Você está com SOBREPESO.')
elif imc < 40:
    print('❗ Você está com OBESIDADE.')
else:
    print('🚨 Você está com OBESIDADE MÓRBIDA.')