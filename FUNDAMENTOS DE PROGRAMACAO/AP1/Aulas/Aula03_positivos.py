positivos = []

for _ in range(6):
    valor = float(input())
    if valor > 0:
        positivos.append(valor)

quantidade_positivos = len(positivos)

if quantidade_positivos > 0:
    media_positivos = sum(positivos) / quantidade_positivos
    print(f"{quantidade_positivos} valores positivos")
    print(f"{media_positivos:.1f}")
else:
    print("0 valores positivos")
    print("0.0")