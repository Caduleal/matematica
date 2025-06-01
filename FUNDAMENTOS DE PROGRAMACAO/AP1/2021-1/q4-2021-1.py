import math
def recebe_pontos():
    linha = input()
    triplas = []
    while linha !="":
        pontos= linha.split()
        if len(pontos)==3:
            x = float(pontos[0])
            y = float(pontos[1])
            z = float(pontos[2])
            triplas.append((x,y,z))
        else:
            print("Erro: Cada linha deve conter 3 numeros")
        linha = input()
    return triplas

def recebe_referencia():
    linha = input("Digite a referência : \n").split()
    if len(linha)==3:
        x = float(linha[0])
        y = float(linha[1])
        z = float(linha[2])
        return (x, y, z)
    else:
        print("Erro: Ponto de referência deve ter 3 coordenadas")
        return recebe_referencia()

def distancia(ponto, referencia):
    return math.sqrt(
        (ponto[0]-referencia[0])**2+
        (ponto[1]-referencia[1])**2+
        (ponto[2]-referencia[2])**2)

def soma_das_distancias(pontos, referencia):
    soma = 0
    for ponto in pontos:
        soma += distancia(ponto, referencia)
    return soma

def imprime_pontos(pontos):
    for ponto in pontos:
        print(f"    ({ponto[0]:.2f}, {ponto[1]:.2f}, {ponto[2]:.2f})")
    return None

def deslocar_pontos(pontos, referencia):
    ciclos = int(input("Digite o número de ciclos: \n"))
    delta = float(input("Digite o delta: \n"))
    for i in range(ciclos):
        novos_pontos = []
        for ponto in pontos:
            novo = tuple(
                ponto[j] + delta*(referencia[j]-ponto[j]) for j in range(3)
            )
            novos_pontos.append(novo)
        pontos = novos_pontos
        print(f"\nApós ciclo {i+1}: ")
        imprime_pontos(pontos)
        soma = soma_das_distancias(pontos, referencia)
        print(f"Soma das Distâncias para o Ponto ({referencia[0]:.2f}, {referencia[1]:.2f}, {referencia[2]:.2f}):")
        print(f"{soma:.2f}")
    return pontos


pontos = recebe_pontos()
referencias = recebe_referencia()
print(f"\nPontos Originais: ")
imprime_pontos(pontos)
soma = soma_das_distancias(pontos, referencias)
print(f"Soma das Distâncias para o Ponto ({referencias[0]:.2f}, {referencias[1]:.2f}, {referencias[2]:.2f}):")
print(f"{soma:.2f}")
deslocar_pontos(pontos, referencias)