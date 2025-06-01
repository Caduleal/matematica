def recebe_numeros():
    numeros = []
    linha = input()
    while linha != "":
        numeros.append(int(linha))
        linha = input()
    return numeros

def conta_repetidos(lista):
    numeros_repetidos = []
    ja_contamos = []
    numeros_unicos=[]
    for numero in lista:
        if numero not in ja_contamos:
            repeticoes = lista.count(numero)
            if repeticoes > 1:
                numeros_repetidos.append((numero, repeticoes))
            else:
                numeros_unicos.append(numero)
            ja_contamos.append(numero)
    return numeros_repetidos, numeros_unicos

def encontrar_mais_repitido(repetidos):
    if len(repetidos) == 0:
        return None
    
    mais_repetido = repetidos[0]
    for i in range(1,len(repetidos)):
        if repetidos[i][1] > mais_repetido[1]:
            mais_repetido = repetidos[i]

    return mais_repetido

def imprime_valores(repetidos, unicos,mais_repetido):
    print("Numeros que aparecem mais de uma vez:")
    for tupla in repetidos:
        print(tupla[0])
    print("Numeros únicos:")
    for numero in unicos:
        print(numero)

    if mais_repetido:
        print(f"Número mais repetido: {mais_repetido[0]} (apareceu {mais_repetido[1]} vezes)")
    else:
        print("Nenhum número repetido")
    print()

numeros = recebe_numeros()
repetidos,unicos=conta_repetidos(numeros)
mais_repetido=encontrar_mais_repitido(repetidos)
imprime_valores(repetidos,unicos,mais_repetido)


