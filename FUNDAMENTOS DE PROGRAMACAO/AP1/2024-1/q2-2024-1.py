def recebe_extremos():
    extremos = input().split()
    for i in range(len(extremos)):
        extremos[i] = float(extremos[i])
    return extremos

def recebe_linhas():
    valores = set()
    linha = input()
    while linha != "":
        numeros = linha.split()
        for i in numeros:
            valores.add(float(i))

        linha=input()
    return valores

def imprime_valores(menor,maior,valores):
    menores = []
    entre = []
    maiores = []

    for valor in valores:
        if valor < menor:
            menores.append(valor)
        elif valor >= menor and valor < maior:
            entre.append(valor)
        else:
            maiores.append(valor)
    print(f"Menores do que {menor}: ")
    for i in menores:
        print("\t",i)
    print()
    print(f"Maiores ou iguais a {menor} e menores que {maior}")
    for i in entre:
        print("\t",i)
    print()
    print(f"Maiores ou iguais a {maior}")
    for i in maiores:
        print("\t",i)
    print()
    return None

a,b = recebe_extremos()
valores= recebe_linhas()
imprime_valores(a,b,valores)
