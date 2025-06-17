num = int(input('Escolha o numero que quer: '))
fator = 1
for c in range(num,0, -1):
    fator *= c
print(fator)

num = int(input('Digite um número para calcular o fatorial: '))
fatorial = 1
contador = num

while contador > 0:
    fatorial *= contador   
    contador -= 1 #diminui o numero ate chegar em 0 fazendo com que saia do while

print(f"O fatorial de {num} é {fatorial}")