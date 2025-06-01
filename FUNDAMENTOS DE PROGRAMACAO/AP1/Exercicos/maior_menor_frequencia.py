def recebe_numeros():
    linha = input()
    valores = []
    while linha != "":
        linha = linha.split()
        for valor in linha: 
            valores.append(int(valor))
        linha = input()
    return valores

def contagem_numeros(lista):
    frequencia = []
    lidos = []
    for numero in lista:
        if numero not in lidos:
            frequencia_num = lista.count(numero)
            frequencia.append((numero,frequencia_num))
            lidos.append(numero)
    return frequencia

def separa_extremo_repetido(lista):
    if len(lista)==0:
        return None
    
    mais_repetido = lista[0]
    menos_repetido = lista[0]

    for i in range(1,len(lista)):
        if lista[i][1] > mais_repetido[1]:
            mais_repetido = lista[i]
        elif lista[i][1]< menos_repetido[1]:
            menos_repetido = lista[i]
    return mais_repetido,menos_repetido

def imprime_valores(mais,menos):
    print(f"O elemento que mais apareceu foi {mais[0]} com {mais[1]} repetições")
    print(f"O elemento que menos apareceu foi o {menos[0]} com {menos[1]} repetições")

numeros = recebe_numeros()
frequencia=contagem_numeros(numeros)
maior,menor=separa_extremo_repetido(frequencia)
imprime_valores(maior,menor)

