while True:
    import math
    print("Vamos calcular as raízes da equação para você!")
    print("Caso a equação seja de primeiro grau, considere a = 0 e b*x + c = 0.")
    a = int(input("Qual é o valor de a: "))
    b = int(input("Qual é o valor de b: "))
    c = int(input("Qual é o valor de c: "))
    if a == 0 and b == 0:
        print("A equação é uma constante e não possui uma raiz.")
        continue
    if a == 0:
        x = (-c)/b
        print(f"A equação é de primeiro grau e x = {x}.")
        continue
    delta = (b**2)-4*a*c
    if delta < 0:
        print("Que pena! A equação não possui raiz real. ")
        continue
    raiz_delta = math.sqrt(delta)
    x1 = (-b+raiz_delta)/(2*a)
    x2 = (-b-raiz_delta)/(2*a)
    if delta == 0:
        print(f"A equação possui somente uma raiz real, sendo x = {x1}. ")
    else:
        print(f"As raízes da equação são x1 = {x1} e x2 = {x2}. ")




