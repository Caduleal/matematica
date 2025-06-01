def recebe_extremos():
    extremos = input().split()
    for i in range(len(extremos)):
        extremos[i] = float(extremos[i])
    return extremos

def recebe_entradas():
    valores = set()
    while True:
        valor= input().strip()
        if valor =="":
            break
        valores_entrada = valor.split()
        for v in valores_entrada:
            valores.add(float(v))
            
    return valores

def imprime_elementos(menor, maior, lista):
    menores= []
    entre = []
    maiores = []
    for numero in lista:
        if numero < menor:
            menores.append(numero)
        elif numero >= menor and numero < maior:
            entre.append(numero)
        else:
            maiores.append(numero)

    print(f"Menores que {menor}:")
    for elemento in menores:
        print(elemento)  
    print(f"Maiores ou iguais a {menor} e Menores que {maior} :")
    for elemento in entre:        
        print(elemento)
    print(f"Maiores ou iguais a {maior}:")
    for elemento in maiores:
        print(elemento)




a,b=recebe_extremos()
valores = recebe_entradas()
imprime_elementos(a,b, valores)