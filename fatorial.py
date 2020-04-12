num = int(input("Digite o numero do fatorial: "))
cont = 1
fat = 1
if num == 0:
    num = 1
while cont <= num:
    fat = fat * cont
    cont = cont + 1
print(fat)

