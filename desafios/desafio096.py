def area(largura, comprimento):
    areaTerreno = (largura * comprimento)
    print(f'A area do terreno é {areaTerreno:.1f}m2')
    
    
print('-'*30)
print('Controle de terronos')
print('-'*30)
l = float(input("Largura (m)"))
m = float(input("comprimento (m)"))
area(l, m)

