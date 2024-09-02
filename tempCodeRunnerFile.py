def soma_binarios(bin1,bin2):
    num1 = int(bin1,2)
    num2 = int(bin2,2)
    soma= num1+num2
    resultado_binario= bin(soma)[2:]
    return resultado_binario
bin1 = input("Digite o primeiro número binário: ")
bin2 = input("Digite o segundo número binário: ")

resultado = soma_binarios(bin1, bin2)
print(f"O resultado da soma é: {resultado}")