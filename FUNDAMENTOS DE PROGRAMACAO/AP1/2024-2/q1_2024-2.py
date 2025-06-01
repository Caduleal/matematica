def recebe_valores():
    valores = []
    while True:
        valor = input()
        if valor == "": 
            break
        valores.append(int(valor))

    return valores

        
def separa_valores(lista):
    pares=[]
    impares=[]
    primos=[]
    for valor in lista:
        divisores = 0

        if valor % 2==0:
            pares.append(valor)
        else:
            impares.append(valor)

        if valor > 1: 
            for i in range(1,valor+1):
                if valor %i == 0: 
                    divisores +=1

        if divisores == 2:
            primos.append(valor) 
    return(pares, impares, primos)
        
def imprime_valores(pares,impares,primos):
    print("Listagem de pares:")
    for i in pares:
        print(i)
    print("Fim da listagem de pares")

    print("Listagem de ímpares:")
    for i in pares:
        print(i)
    print("Fim da listagem de ímpares")

    print("Listagem de primos: ")
    for i in primos:
        print(i)
    print("Fim da listagem de primos")
    print("Obrigado por utilizar nosso sistema!!")


valores = recebe_valores()
pares, impares, primos = separa_valores(valores)
imprime_valores(pares, impares,primos)