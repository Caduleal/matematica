def recebe_numeros():
    linha = input()
    numeros = []
    while linha != "":
        linha = linha.split()
        for i in range(len(linha)):
            numeros.append(int(linha[i]))
        linha = input()
    return numeros

def separa_valores(numeros):
    pares = []
    impares = []
    primos = []

    for numero in numeros:
        contador = 0
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
        for i in range(1,numero+1):
            if numero % i == 0:
                contador += 1
        if contador == 2:
            primos.append(numero)
    return pares, impares, primos

def imprime_numeros(par, impar, primo):
    print("Listagem de pares")
    for numero in par:
        print(numero)
    print("Fim da listagem de pares")
    print("Listagem de impares")
    for numero in impar:
        print(numero)
    print("Fim da listagem de impares")
    print("Listagem de primos")
    for numero in primo:
        print(numero)
    print("Fim da listagem de primos")
    print("Obrigado por utilizar nosso sistema!")
    return None

valores = recebe_numeros()
par, impar, primo = separa_valores(valores)
imprime_numeros(par, impar, primo)