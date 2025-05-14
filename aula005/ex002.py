num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: ")) 
res = num1 + num2
res1 = num1 - num2
res2 = num1 * num2
res3 = num1 / num2
res4 = num1 ** num2
res5 = num1 // num2
res6 = num1 % num2

if res%2 == 0:
    print("O numero {} é par".format(res), end=' ')
else: 
    print("O numero {} é inpar ".format(res), end=' ')
    
      #---------------------------------
      
if res1%2 == 0:
    print("O numero {} é par".format(res1))
else:
    print("O numero {} é inpar ".format(res1))
    
    #---------------------------------
    
if res2%2 == 0:
    print("O numero {} \n é par".format(res2))
else:
    print("O numero {} \n é inpar ".format(res2))
    
    #---------------------------------
    
if res3%2 == 0:
    print("O numero {:.3f} é par".format(res3))
else:
    print("O numero {:.3f} é inpar ".format(res3))
    
    #---------------------------------
    
if res4%2 == 0:
    print("O numero {} é par".format(res4))
else:
    print("O numero {} é inpar ".format(res4))

    #---------------------------------
    
if res5%2 == 0:
    print("O numero {} é par".format(res5))
else:
    print("O numero {} é inpar ".format(res5))
    
    #---------------------------------
    
if res6%2 == 0:
    print("O numero {} é par".format(res6))
else:
    print("O numero {} é inpar ".format(res6))
