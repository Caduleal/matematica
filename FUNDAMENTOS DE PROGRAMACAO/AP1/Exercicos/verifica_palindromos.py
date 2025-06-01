def recebe_linha():
    linha = input().strip()
    palindromos = []
    while linha != "":
        n = len(linha)-1
        if verifica_palindromos(linha, 0,n):
            palindromos.append(linha)
        linha = input().strip()
    return palindromos

def verifica_palindromos(lista, i ,n):
    if i >=n:
        return 1
    if lista[i]!= lista[n]:
        return 0
    return verifica_palindromos(lista,i+1,n-1)

def imprime_valores(lista):
    print("Palíndromos: ")
    for elemento in lista:
        print(elemento)

valores =recebe_linha()
imprime_valores(valores)