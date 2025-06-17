def fatorial(n, show=False):
    """
    Calcula o fatorial de um número.
    
    Parâmetros:
    n (int): número a ser calculado.
    show (bool): mostra ou não o processo. Padrão é False.
    
    Retorna:
    int: o resultado do fatorial.
    """
    f = 1
    for i in range(n, 0, -1):
        f *= i
        if show:
            print(i, end=' x ' if i > 1 else ' = ')
    return f


# Exemplo de uso:
numero = int(input("Digite um número para calcular o fatorial: "))
mostrar = input("Deseja mostrar o processo? [S/N] ").strip().lower()

# Converte 's' para True, qualquer outra coisa será False
mostrar_processo = mostrar == 's'

resultado = fatorial(numero, show=mostrar_processo)
print(resultado)