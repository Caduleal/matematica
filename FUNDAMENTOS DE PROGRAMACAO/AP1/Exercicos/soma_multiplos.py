def recebe_valores():
    linha = input()
    valores = []
    while linha != "":
        partes = linha.split()
        for p in partes:
            valores.append(int(p))
        linha= input()
    return valores

def separa_multiplos(lista,n):
    multiplos = []
    for numero in lista:
        if numero % n == 0:
            multiplos.append(numero)
    return multiplos

def imprime_soma(lista,n):
    print(f"Soma dos multipos de {n}")
    print(lista)
    print(f"{sum(lista)}")

valores = recebe_valores()
multiplos_5=separa_multiplos(valores,5)
imprime_soma(multiplos_5,5)
multiplos_3=separa_multiplos(valores,3)
imprime_soma(multiplos_3,3)