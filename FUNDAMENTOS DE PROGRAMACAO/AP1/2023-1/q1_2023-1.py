def recebe_valores():
    valores = []
    linha = input()
    while linha != "":
        valores.append(int(linha))
        linha = input()
    return valores

def separa_valores(valores):
    par = []
    impar = []
    primo = []

    for numero in valores:
        divisores = 0
        if numero %2 == 0:
            par.append(numero)
        else:
            impar.append(numero)

        for i in range(1,numero+1):
            if numero % i ==0:
                divisores+=1

        if divisores == 2:
            primo.append(numero)
            
    return par, impar, primo
            
def imprime_valores(par, impar, primo):
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
        
lista =recebe_valores()
par,impar,primo=separa_valores(lista)
imprime_valores(par,impar,primo)