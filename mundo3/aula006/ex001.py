import uteis as numeros

num = int(input('Digite um valor: '))

fat = numeros.fatorial(num)
tri = numeros.triplo(num)
dobro = numeros.dobro(num)
raiz = numeros.math.sqrt(num)

print(f'O fatorial de {num} é {fat}')
print(f' o triplo de { num } é {tri}')
print(f' o dobro de { num } é {dobro}')
print(f'{raiz}')