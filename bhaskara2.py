import math as m

a = float(input("Digite o A:"))
b = float(input("Digite o B:"))
c = float(input("Digite o C:"))


def delta(a, b, c):
    return (m.pow(b, 2)) - (4 * a * c)


def x1(d, a, b):
    return (-b + m.sqrt(d)) / (2 * a)


def x2(d, a, b):
    return (-b - m.sqrt(d)) / (2 * a)


d = delta(a, b, c)


if d > 0:
    x1 = x1(delta(a, b, c), a, b)
    x2 = x2(delta(a, b, c), a, b)
    if x1 > x2:
        print("as raízes da equação são", x2, "e", x1)
    else:
        print("as raízes da equação são", x1, "e", x2)
elif d == 0:
    print("a raiz desta equação é", x1)
else:
    print("esta equação não possui raízes reais")
