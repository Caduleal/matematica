def recebe_valores():
    linha = input()
    soma=0
    total=0
    while linha != "":
        valores = linha.split()
        for i in range (len(valores)):
            valores[i]= float(valores[i])
            soma += valores[i]
            total+=1
        verifica_extremos(valores)
        linha = input()

    media = soma/total
    print(f"Quantidade de numeros lidos {total}")
    print(f"Média dos numeros lidos: {media:.2f}")

def verifica_extremos(linha):
    menor = linha[0]
    maior = linha[0]
    for num in linha:
        if num < menor:
            menor = num 
        elif num > maior:
            maior = num
    
    print(f"Menor: {menor} Maior: {maior}")

recebe_valores()