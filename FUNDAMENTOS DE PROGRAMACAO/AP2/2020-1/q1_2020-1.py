def processa_mostra_extremos(linha_numeros):
    numeros = linha_numeros.split()
    for i in numeros:
        numeros[i] = float(numeros[i])
    soma_linha = 0
    maior = menor = numeros[0]
    for valor in numeros:
        if valor > maior:
            maior = valor 
        elif valor < menor:
            menor = valor
        soma_linha+= valor
    print("Maior = " ,maior, "Menor =", menor)
    return len(numeros), soma_linha

qtd_numeros = 0
soma_numeros = 0
linha = input()
while linha != "":
    qtd_numeros_linha, soma_numeros_linha = processa_mostra_extremos(linha)
    qtd_numeros += qtd_numeros_linha
    soma_numeros+=soma_numeros_linha
    linha = input()
print("Quantidade de números lidos: ",qtd_numeros)
if qtd_numeros == 0:
    print("Nenhum numero foi lido, portanto não existe média")
else:
    print(f"Média dos numeros lidos: {soma_numeros/qtd_numeros:.2f}")

    