dias = float(input("Por quantos dias ficou com o carro: "))
pdia = 60 *dias

km = float(input("Quantos Km você rodou com o carro: "))
pkm = 0.15 * km

total = pdia + pkm

print("Voce Rodou {} dias por dia o valor do carro é R$60 ficando um total de R${}\nVocê rodou {}Km por km rodado o valor é R$0.15 ficando um total de R${:.2f}\nJuntado os dois valores pagos saindo R${:.2f}".format(dias,pdia,km,pkm,total))