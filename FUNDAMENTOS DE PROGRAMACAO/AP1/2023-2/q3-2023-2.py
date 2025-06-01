def recebe_valores():
    linha = input().split()
    for i in range(len(linha)):
        linha[i]= int(linha[i])

    return linha

def separa_extremos_media(linha):
    menor = linha[0]
    maior = linha[0]
    soma_pares = 0
    pares = 0
    
    for elemento in linha:
        if elemento % 2 ==0:
            pares +=1
            soma_pares += elemento

        if elemento < menor:
            menor = elemento
        elif elemento > maior:
            maior = elemento

    if pares == 0:
        media = 0
    else:
        media = soma_pares/pares
    return imprime_extemos_media(menor, maior, media)

def imprime_extemos_media(menor, maior, media):
    print(f"Menor: {menor}")
    print(f"Maior: {maior}")
    print(f"Média dos pares: {media:.1f}")
    return None

linha = recebe_valores()
separa_extremos_media(linha)
