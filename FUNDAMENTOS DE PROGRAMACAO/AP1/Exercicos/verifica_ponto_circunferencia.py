def recebe_circunferencia():
    linha = input().split()
    if len(linha) !=3:  
        print("Por favor digite as coordenadas (x,y) e o raio r: ")
        return recebe_circunferencia()
    circunferencia = []
    for i in range(len(linha)):
        circunferencia.append(float(linha[i]))
    return circunferencia

def recebe_pontos():
    pontos = []
    linha = input("Digite um ponto(x,y) ou enter para parar: \n")
    while linha != "":
        linha = linha.split()
        if len(linha) == 2:
            x = float(linha[0])
            y = float(linha[1])
            pontos.append((x,y))
        else:
            print("Cada ponto deve ter duas coordenadas (x,y).")
        linha = input()
    return pontos

def verifica_pontos(pontos, circunferencia):
    x0, y0, r = circunferencia
    for ponto in pontos:
        x, y = ponto
        distancia_quadrado = (x - x0)**2 + (y - y0)**2
        raio_quadrado = r**2

        if distancia_quadrado < raio_quadrado:
            print("Dentro")
        elif distancia_quadrado == raio_quadrado:
            print("Na borda")
        else:
            print("Fora")
    return None

circunferencia = recebe_circunferencia()
pontos = recebe_pontos()
verifica_pontos(pontos, circunferencia)


