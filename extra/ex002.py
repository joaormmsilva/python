venda = int(input('Valor do produto: '))

if venda < 10:
    lucro = venda * 0.70
elif venda < 30:
    lucro = venda * 0.50
elif venda < 50:
    lucro = venda * 0.40
else:
    lucro = venda * 0.30

print('Nessa compra o lucro foi de R$ {:.2f} pois a compra foi no valor R$ {:.2f}'.format(lucro,venda))