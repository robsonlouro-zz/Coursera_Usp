num = int(input("Digite um número inteiro: "))
igual = False
anter = num % 10
num = num // 10
dig = 0
while num > 0 and not igual:
    atual = num % 10
    num = num// 10
    if atual == anter:
        igual = True
    anter = atual
if igual:
    print("sim")
else:
    print("não")
