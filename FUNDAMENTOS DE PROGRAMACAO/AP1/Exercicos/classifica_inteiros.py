def recebe_inteiros():
    linha = input()
    numeros=[]
    while linha != "":
        numeros.append(int(linha))
        linha = input()
    return numeros

def separa_inteiros(numeros):
    positivos= []
    negativos = []
    for num in numeros:
        if num >= 0:
            positivos.append(num)
        else:
            negativos.append(num)
    return positivos, negativos

def imprime_valores(postivos, negativos):
    total = len(postivos)+len(negativos)
    print(f"Positivos: {postivos}")
    print(f"Negativos: {negativos}")
    print(f"Quantidade total: {total}")
    return None


lista = recebe_inteiros()
positivos, negativos=separa_inteiros(lista)
imprime_valores(positivos, negativos)