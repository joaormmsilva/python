saldo = float(input("Digite o quanto vc tem na carteira: "))
convert = saldo / 5.67

print("O sando que você possui atualmente é R${:.2f} Reais\nEsse valor pode ser convertido em US${:.2f} Dolares\nPois atualmente 1 dolar equivale a 5.67 Reias".format(saldo, convert))