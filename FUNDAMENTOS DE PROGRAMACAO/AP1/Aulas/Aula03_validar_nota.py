nota01 = float(input())
while nota01 < 0 or nota01 > 10:
    print("Nota Inválida")
    nota01 = float(input())

nota02 = float(input())
while nota02 < 0 or nota02 > 10:
    print("Nota Inválida")
    nota02 = float(input())

media = (nota01 + nota02)/2
print(f"Média = {media:.2f}")