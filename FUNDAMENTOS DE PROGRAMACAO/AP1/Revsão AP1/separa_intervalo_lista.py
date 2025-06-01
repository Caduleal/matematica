def serpara_extremos():
    linha = input().split()
    min = float(linha[0])
    max = float(linha[1])
    return min, max

def recebe_numeros():
    numeros = set()
    linha = input()
    while linha != "":
        linha = linha.split()
        for i in range(len(linha)):
            numeros.add(float(linha[i]))
        linha = input()
    return numeros

def separa_imprime_intervalo(numeros, min,max):
    menores = []
    entre = []
    maiores = []
    for numero in numeros:
        if numero < min:
            menores.append(numero)
        elif numero >= max:
            maiores.append(numero)
        else:
            entre.append(numero)

    print(f"Menores que {min}")
    for numero in menores:
        print(numero)

    print(f"\nMaiores ou iguais a {min} e maiores que {max}: ")
    for numero in entre:
        print(numero)

    print(f"\nMaiores ou iguais a {max}")
    for numero in maiores:
        print(numero)

menor, maior = serpara_extremos()
valores = recebe_numeros()
separa_imprime_intervalo(valores, menor, maior)