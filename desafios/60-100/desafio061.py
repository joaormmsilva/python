primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

contador = 1
total = 10
termo = primeiro

while total != 0:
    while contador <= total:
        print(f'{termo}', end=' → ')
        termo += razao
        contador += 1
    print('PAUSA')
    total = int(input('Quantos termos você quer mostrar a mais? (Digite 0 para sair): '))
    contador = 1  # Resetar o contador para contar os novos termos

print('FIM DA PA')
