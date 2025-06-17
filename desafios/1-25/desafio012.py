preço = float(input("Qual o valor do produto: "))
desconto = (-preço * 0.05) + preço

print("O preço do seu produto é {} e ele com 5% de desconto é {:.2f}". format(preço, desconto))