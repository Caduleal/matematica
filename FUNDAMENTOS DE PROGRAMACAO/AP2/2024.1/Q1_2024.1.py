def le_arquivo():
    arquivo = input()
    lista_de_listas = list()
    with open(arquivo, 'r') as fin:
        for linha in fin:
            lista_de_listas.append(list(map(int, linha.split())))
    return lista_de_listas

def verifica_restricao(lin,col,matriz):
    for linha in [ lin-1, lin,lin+ 1]:
        for coluna in[col-1,col,col+1]:
            if 0 <= linha < len(matriz) and 0 <= coluna <len(matriz[0]) and (linha,coluna) != (lin,col) and matriz[lin][col] >= matriz[linha][coluna]:
                return False
    return True

def adjacentes_maiores(matriz):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if verifica_restricao(linha,coluna, matriz):
                print(f"Linha ={linha+1}, Coluna = {coluna+1}, valor = {matriz[linha][coluna]}")
    return None
valores = le_arquivo()
adjacentes_maiores(valores)
