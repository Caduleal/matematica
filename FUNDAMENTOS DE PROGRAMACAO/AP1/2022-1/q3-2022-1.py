def verifica_float(entrada):
    valores = ['0','1','2','3','4','5','6','7','8','9','.']
    for i in range(0,len(entrada)):
        if entrada[i] not in valores:
            print(f"Você digitou errado {entrada} não é do tipo float.")
            return False
    pontos = entrada.count(".")
    if pontos > 1:
        print("Há mais do que um ponto '.'")
        return False
    return transforma_float(entrada)

def transforma_float(numero):
    numero = float(numero)
    return numero 

def converte(valor):
    taxa = float(input())
    convertido = valor*taxa
    print(f"O valor {valor} com a taxa {taxa} vai para {convertido:.3f}")
    return parcelar(convertido)

def parcelar(valor):
    parcelas = int(input(f"Em quantas vezes voce deseja parcelar o valor {valor}:\n"))
    if parcelas == 1:
        return desconto(valor)
    valor_total=valor
    for i in range(2,parcelas):  
        valor_total *= 1.05  
    print(f"Pagando em {parcelas} parecelas e com 5% de juros ao mês, você pagará {valor_total/parcelas:.2f}sendo o total de {valor_total:.2f}.")
    
def desconto(valor):
    valor_final=valor -valor*.15
    print(f"Voce ganhou 15% de desconto, portanto de {valor:.2f} você vai pagar {valor_final:.2f}")

def main():
    valor = input()
    valor = verifica_float(valor)
    if valor == False:
        main()
    converte(valor)

main()