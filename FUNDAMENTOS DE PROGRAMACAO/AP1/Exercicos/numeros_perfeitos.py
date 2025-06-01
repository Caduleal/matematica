def recebe_numeros():
    linha = input()
    numeros = []
    while linha != "":
        linha = linha.split()
        for numero in linha:
            numeros.append(int(numero))
        linha = input()
    return numeros

def verifica_perfeitos(lista):
    numeros_perfeitos=[]
    for numero in lista:
        divisores=[]
        for i in range(1,numero):
            if numero %i ==0:
                divisores.append(i)
        total = sum(divisores)
        if total == numero:
            numeros_perfeitos.append(numero)
    return numeros_perfeitos

def imprime_valores(numeros):
    print(f"Quantidade de numeros perfeitos encontrados: {len(numeros)}")
    print(f"Numeros perfeitos: ")
    for numero in numeros:
        print(numero)
    print("Muito obrigado por utilizar o sistema!")

valores = recebe_numeros()
numeros_perfeitos = verifica_perfeitos(valores)
imprime_valores(numeros_perfeitos)
    

