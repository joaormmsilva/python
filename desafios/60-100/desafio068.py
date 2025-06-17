import random
computador = int(random.randint(1, 100))
vitoria = 0
while True:
    conta = input("Vamos jogar um jogo de Impar ou Par\nEscolha qual quer [impar/par]: ").lower()
    jogador = int(input('Escolha seu numero: '))
    res = jogador + computador
    print(f'Você jogou {jogador} e eu joguei {computador} dando {res}')
    print('\n')
    if res % 2 == 0 and conta == "par" or res % 2 == 1 and 'impar':
        print('Você venceu')
        vitoria += 1
        conta = input("Vamos novamente escolha [impar/par]: ")
        jogador = int(input('Escolha seu numero: '))
        print(f'Você jogou {jogador} e eu joguei {computador} dando {res}')
        print('\n')
        
    if res % 2 == 0 and conta == "impar" or res % 2 == 1 and 'par':
        break
print('\nVoce perdeu para mim')
print(f"Você ganhou {vitoria} vezes mas depois disso tudo eu ganhei")
        
    