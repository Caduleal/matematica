def recebe_clientes():
    linha = input()
    clientes = []
    while linha != "":
        clientes.append([linha])
        linha = input()
    return clientes

def recebe_informações_cliente(lista):
    for cliente in lista:
        idade = int(input(f"Digite a idade de {cliente[0]}"))
        telefone = input(f"Telefone de {cliente[0]}")
        email = input(f"Email de {cliente[0]}")
        cliente.extend([idade,telefone,email])

    return lista

def main():
    matriz_cliente = recebe_clientes()
    recebe_informações_cliente(matriz_cliente)

    print("\nMatriz de clientes: ")
    for cliente in matriz_cliente:
        print(cliente)

main()