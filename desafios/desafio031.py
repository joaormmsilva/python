distancia = float(input('Qual a distancia do seu destino: '))
if distancia > 200:
    valor = distancia * 0.45
    print('O valor da sua passagem é {:.2f} pois a distancia é {:.2f}'.format(valor, distancia))
else:
    valor = distancia * 0.50
    print('O valor da sua passagem é {:.2f} pois a distancia é {:.2f}'.format(valor, distancia))
    
