valores = []
for c in range(5):
    valor = int(input(f'digite o {c+1}° valor: '))
    valores.append(valor)
    valores.sort()
    print(valores)

