valores = []
for c in range(5):
    valor = int(input(f'digite o {c+1}° valor: '))
    valores.append(valor)
    valores.sort()
    print(valores)

lista = []

for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    if not lista or num > lista[-1]:
        lista.append(num)
        print("Adicionado ao final da lista.")
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f"Adicionado na posição {pos}.")
                break
            pos += 1

print(f"\nOs valores ordenados são: {lista}")
