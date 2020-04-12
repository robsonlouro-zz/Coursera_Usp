def fatorial(num):

    cont = 1
    fat = 1
    if num == 0:
        num = 1
    while cont <= num:
        fat = fat * cont
        cont = cont + 1
    return(fat)

def binomial(n,k):
    return fatorial(n) / (fatorial(k) * (fatorial(n - k)))

k=1
n=0
while k > n:
    n = int(input("Digite o primeiro termo: "))
    k = int(input("Digite o segundo termo: "))
if (n == k) or (k == 0) or (k == 1):
    coef = 1
    print("Sem cálculo")
else:
    coef = binomial(n,k)
print(coef)