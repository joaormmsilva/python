def dobrar(n):
    dobro = n *2
    return dobro

def metade(n):
    metade = n / 2
    return metade

def aumentar(porMais, n):
    porcento = porMais / 100
    aumento = (n * porcento) + n
    
    return aumento

def diminuir(porMenos, n):
    porcento = porMenos / 100
    print(porcento)
    diminui = ((n * porcento) - n) * -1
    return diminui
    