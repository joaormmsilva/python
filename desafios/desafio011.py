largura = float(input("Digite qual é a largura da parede que deseja: "))
altura = float(input("Digite qual é a altura da parede que deseja: "))
area = largura * altura
tinta = area / 2

print("Para pintar essa parece vai ser necessario {:.f2}m²".format(tinta))