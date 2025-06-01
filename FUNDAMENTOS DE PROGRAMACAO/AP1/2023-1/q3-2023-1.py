def recebe_valores():
    linha = input("Entre com o elemento para aplicar a função de Collatz\n")
    if linha.isdigit() and int(linha) > 0:
        return int(linha)  
    print("Valor não é inteiro ou positivo")
    return recebe_valores()
    
def collatz(numero):
    if numero %2 ==0:
        resultado=numero/2
    else:
        resultado= 3*numero+1
    return int(resultado)

def sequencia_collatz(numero):
    sequencia = []
    while numero !=1:
        numero = collatz(numero)
        sequencia.append(numero)
    return sequencia

def imprime_collatz(numero):
    primeiro_resultado = collatz(numero)
    print(f"Aplicando a função de Collatz ao {numero}, temos: {primeiro_resultado}")
    print(f"Além disso, a sequência de Collatz de {numero} é: ")
    sequencia =sequencia_collatz(numero)
    for numero in sequencia:
        print(numero, end=" ")
    print()
    return None

def sequencia_outros(numero):
    print(f"A conjectura da Collatx de 3 até {numero} é verdadeira, pois: ")
    for i in range(3,numero+1):
        sequencia=sequencia_collatz(i)
        for numero in sequencia:
            print(numero, end=" ")
        print()
    return None

valor=recebe_valores()
imprime_collatz(valor)
sequencia_outros(valor)


