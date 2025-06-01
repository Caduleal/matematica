saldo = 200.00
mensagem =   """
    [1] - Depositar
    [2] - Sacar
    [3] - Consultar Saldo
    [4] - Sair
    """
linha = input(f"{mensagem}")
while not (linha.isdigit() and 1<=int(linha)<=4):
    print("Entrada invalida. Digite um numero inteiro")
    linha = input(f"{mensagem}")

linha = int(linha)
while linha != 4 :
    linha = int(linha)
    if linha ==1 :
        print("Depositar")
        deposito = float(input("Digite o valor do depósito :"))
        if deposito > 0 :
            saldo = saldo + deposito
        else:
            print("Digite um número maior que zero para depositar.")
    elif linha == 2 :
        print("Sacar")
        saque = float(input("Digite o valor de saque :"))
        if saque <= saldo :
            saldo = saldo - saque 
        else :
            print("O valor do saque é maior que o saldo.")
    elif linha == 3:
        print("Consultar saldo")
        print(f"Seu saldo é : {saldo}")

    linha =input(f"{mensagem}" )
    while not (linha.isdigit() and 1<=int(linha)<=4):
        print("Entrada invalida. Digite um numero inteiro")
        linha=input(f"{mensagem}")
    linha = int(linha)
    
print("Sair")