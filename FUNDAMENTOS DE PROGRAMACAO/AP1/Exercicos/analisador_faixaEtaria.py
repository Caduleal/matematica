def recebe_idades():
    linha = input()
    idades = []
    while linha != "":
        linha = linha.split()
        for idade in linha:
            idades.append(int(idade))
        linha = input()
    return idades

def separa_idades(idades):
    menores = []
    adultos = []
    idosos = []
    for idade in idades:
        if idade <= 18:
            menores.append(idade)
        elif idade >60:
            idosos.append(idade)
        else:
            adultos.append(idade)
    return menores, adultos, idosos

def imprime_valores(menores,adultos, idosos):
    print(f"Quantidade de menores de idade:{len(menores)}")
    print(f"Quantidade de adultos:{len(adultos)}")
    print(f"Quantidade de idosos:{len(idosos)}")

idades = recebe_idades()
menores, adultos, idosos = separa_idades(idades)
imprime_valores(menores, adultos, idosos)