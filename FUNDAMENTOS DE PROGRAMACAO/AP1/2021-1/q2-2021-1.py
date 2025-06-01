def recebe_nomes():
    nomes = []
    linha = input()
    while linha != "":
        linha = linha.strip()
        nomes.append(linha)
        linha = input()
    return nomes

def encurta_nomes(nomes):
    nomes_encurtados = []
    palavras_excuidas = {"e", "de", "da", "das","do","dos"}
    for nome in nomes:
        partes = nome.split()
        novo_nome = []
        for i in range(len(partes)):
            palavra = partes[i]
            if i == 0 or i == len(partes)-1:
                novo_nome.append(palavra)
            elif palavra.lower() in palavras_excuidas:
                continue
            elif len(palavra) > 3:
                novo_nome.append(palavra[0]+".")
            else:
                continue
        nomes_encurtados.append(novo_nome)
    for nomes in nomes_encurtados:
        print()
        for i in range(len(nomes)):
            print(nomes[i], end=" ")
    return None

lista_nomes = recebe_nomes()
encurta_nomes(lista_nomes)