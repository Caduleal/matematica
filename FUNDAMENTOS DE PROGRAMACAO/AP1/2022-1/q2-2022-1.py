def processa_nome():
    linha = input().split()
    print(linha[0], linha[len(linha)-1])
    return None

total = int(input())
for i in range(total):
    processa_nome()
