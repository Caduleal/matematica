def verifica_palindromo(lista, i, n):
    if i >= n:
        return 1
    if lista [i] != lista[n]:
        return 0
    return verifica_palindromo(lista, i+1,n-1)


def recebe_linha():
    linha = input().strip()
    while linha != "":
        n= len(linha)-1
        if verifica_palindromo(linha,0,n):
            print(linha)
        linha=input().strip()
    
recebe_linha()