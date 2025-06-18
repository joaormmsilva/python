from random import randint

print('-' * 40)
print('Vamos jogar ímpar ou par')

vitorias = 0  # Contador de vitórias do jogador

while True:
    tipo = input('Escolha (impar/par): ').strip().lower()
    while tipo not in ['impar', 'par']:
        tipo = input('Opção inválida! Escolha "impar" ou "par": ').strip().lower()

    numero = int(input('Escolha um número: '))
    computador = randint(1, 3)
    print('-' * 40)
    print(f'Você jogou {numero} e o computador jogou {computador}. Total = {numero + computador}')

    total = numero + computador

    if total % 2 == 0:
        resultado = 'par'
    else:
        resultado = 'impar'

    print(f'O resultado foi {resultado.upper()}')

    if resultado == tipo:
        print('Parabéns, você ganhou!')
        vitorias += 1
    else:
        print('O computador ganhou!')
        break

    print('-' * 40)

print('-' * 40)
print(f'Jogo finalizado! Você venceu {vitorias} vezes consecutivas.')
