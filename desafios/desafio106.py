def ajuda(comando):
    help(comando)


while True:
    print('-' * 40)
    cmd = input('Digite um comando ou função (ou FIM para sair): ').strip()
    if cmd.upper() == 'FIM':
        print('Encerrando o programa...')
        break
    else:
        ajuda(cmd)
