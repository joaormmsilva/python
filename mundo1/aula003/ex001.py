num1 = int(input("Digite o primeiro numero: "))
print(type(num1))
num2 = int(input("Digite o segundo numero: "))
print(type(num2))
res = num1 + num2

if res >= 10:
    print("o resultado de {} + {} é {} sendo igual ou maior que 10".format(num1,num2,res))
elif res == 0:
    print("o resultado de {} + {} é {} sendo 00".format(num1,num2,res))
else: 
    print("o resultado de {} + {} é {} sendo menor que 10".format(num1,num2,res))