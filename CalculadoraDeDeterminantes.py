def criar_matriz(num_linhas, num_colunas):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = int(input("Digite o elemento[" + str(i) + "][" + str(j) + "]"))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def calcular_determinante(matriz):
    if len(matriz) == 1:
        return matriz[0][0]
    
    if len(matriz) == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    
    determinante = 0
    for c in range(len(matriz)):
        submatriz = [linha[:c] + linha[c+1:] for linha in (matriz[1:])]
        cofator = ((-1) ** c) * matriz[0][c] * calcular_determinante(submatriz)
        determinante += cofator
    return determinante
    

def le_matriz():
    lin = int(input("Digite o numero de linhas para a matriz: "))
    col = int(input("Digite o numero de colunas para a matriz: "))
    matriz = criar_matriz(lin, col)
    
    print("Matriz inserida:")
    for linha in matriz:
        for elemento in linha:
            print(elemento, end="\t")
        print()
    
    if lin == col:
        determinante = calcular_determinante(matriz)
        print(f"Determinante da matriz: {determinante}")
    else:
        print("A matriz não é quadrada, portanto a determinante não pode ser calculada.")

    return matriz
while True:
    le_matriz()