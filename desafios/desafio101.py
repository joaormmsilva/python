import datetime
def voto(ano):
    if idade <= 16:
        return "Negado"
    elif idade <18:
        return "Opcional"
    elif idade < 65:
        return "Obrigatorio"
    else:
        return "Opcional"
    


nascimento  = int(input("digite sua dade de nascimento: "))

anoAtual = datetime.datetime.now().year
idade = anoAtual - nascimento

resultado = voto(idade)
print(f'Com {idade} anos: {resultado}')