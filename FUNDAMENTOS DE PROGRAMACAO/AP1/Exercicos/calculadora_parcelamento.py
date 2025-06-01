def recebe_valor():
    valor = float(input("Digite o valor do produto: \n"))
    parcelas = int(input("Digite a quantidade de parcelas: \n"))
    if parcelas ==1:
        return desconto(valor)
    else:
        return valor,parcelas
    
def desconto(valor):
    valor = valor -valor*.15
    return valor

def parcela_valor(valor, tempo):
    valor_final = valor
    for i in range(2,tempo+1):
        valor_final*= 1.015
    return valor_final

def imprime_simulacao(valor,tempo):
    for i in range(1,tempo+1):
        if i ==1:
            print(f"{i}X de R$ {desconto(valor)} (15% de desconto à vista)")
        print(f"{i}X de {parcela_valor(valor,i)/i:.2f} (Total: R${parcela_valor(valor,i):.2f})")

valor,tempo = recebe_valor()
imprime_simulacao(valor,tempo)