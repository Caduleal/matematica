import math
def recebe_valores():
    pontos = int(input())
    vetor = []
    for i in range(pontos):
        linha = input().split()
        x = float(linha[0])
        y = float(linha[1])
        vetor.append((x,y))
    recebe_coordenadas(vetor)

def ponto_dentro_circunferencia(ponto, centro,raio):
    distancia = math.sqrt((ponto[0]-centro[0])**2+(ponto[1]-centro[1])**2)
    return distancia <= raio

def recebe_coordenadas(vetor):
    while True:
        linha = input().split()
        xCirc = float(linha[0])
        yCirc = float(linha[1])
        rCirc = float(linha[2])
        if xCirc == 0 and yCirc == 0 and rCirc == 0:
            break

        centro = (xCirc,yCirc)
        print(f"Contidos na circunferência com centro ({centro[0]},\n{centro[1]}) e raio {rCirc}:")
        for ponto in vetor:
            if ponto_dentro_circunferencia(ponto, centro, rCirc):
                print(f"{ponto[0]} {ponto[1]}")
        print()
    print("Obrigado por utilizar nosso sistema!!")

recebe_valores()
