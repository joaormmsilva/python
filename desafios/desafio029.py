vel = float(input('Qual velocidade do seu carro: '))
multa = (vel - 80) * 7

if vel > 80:
    print('Sua velocidade esta acima do limite da via (80Km)')
    print('Voce foi multado em R${} pois estava a {}Km/h'.format(multa, vel))
else:
    print('dirija sempre com segurança')