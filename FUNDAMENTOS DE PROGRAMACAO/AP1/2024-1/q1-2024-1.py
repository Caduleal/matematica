def numero_linhas():
    numero = int(input())
    return numero

def conta_digitos(texto):
    qtd_digitos = 0
    qtd_outros = 0
    for caracter in texto:
        if '0' <= caracter <="9":
            qtd_digitos+=1
        else:
            qtd_outros +=1
    return qtd_digitos,qtd_outros

def recebe_linhas(numero):
    linhas_validas = []
    for i in range(numero):
        linha=input()
        qtd_digitos, qtd_outros = conta_digitos(linha)
        if qtd_digitos > qtd_outros:
            linhas_validas.append(linha)
    for linha in linhas_validas:
        print(linha)

numero = numero_linhas()
recebe_linhas(numero)




