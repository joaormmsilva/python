s = 0
cont = 0
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        cont = cont +1
        s += c

print(cont)
print(s)