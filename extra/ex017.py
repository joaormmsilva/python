def verifica_palindromo(texto):
    texto = texto.lower().replace(' ', '')  # Deixa tudo minúsculo e sem espaços
    if texto == texto[::-1]:  # Compara o texto com ele mesmo de trás pra frente
        return True
    else:
        return False

# Exemplo de uso
frase = input('Digite uma palavra ou frase: ')
if verifica_palindromo(frase):
    print('É um palíndromo!')
else:
    print('Não é um palíndromo.')
