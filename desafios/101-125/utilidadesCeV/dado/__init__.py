def leiaDinheiro(msg):
    while True:
        entrada = input(msg).strip()

        # Substituir vírgula por ponto para permitir separador decimal brasileiro
        entrada = entrada.replace(',', '.')

        # Verificar se está vazio ou só espaços
        if entrada == '':
            print('\033[31mERRO! Digite um valor numérico válido.\033[m')
            continue

        # Tentar converter para float
        try:
            valor = float(entrada)
            return valor
        except ValueError:
            print('\033[31mERRO! Digite um número válido.\033[m')
