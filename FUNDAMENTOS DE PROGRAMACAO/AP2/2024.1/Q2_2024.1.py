def recebe_arquivo_nomes():
    arquivo = input("")
    nomes = dict()
    sobrenomes = dict()
    with open(arquivo,'r',encoding="utf-8") as fin:
        linhas = fin.readlines()
        if not linhas:
            print("Arquivo Vazio!")
            return None ,None
        for linha in linhas:
            nome_completo = linha.strip("\n").split()
            nome = nome_completo[0]
            sobrenome = nome_completo[-1]
            if nome in nomes:
                nomes[nome] += 1
            else:
                nomes[nome] = 1
            if sobrenome in sobrenomes:
                sobrenomes[sobrenome] += 1
            else:
                sobrenomes[sobrenome] = 1
    return nomes, sobrenomes

def busca_moda(dicionario):
    moda = 0
    for elemento in dicionario:
        if dicionario[elemento] > moda:
            moda = dicionario[elemento]
    return moda

def imprime_moda(label, valor, dicionario):
    print(f"{label}(s) da Moda:")
    for elemento in sorted(dicionario):
        if dicionario[elemento] == valor:
            print(f"{elemento} (aparece {valor} vez(es))")
    return None

nomes,sobrenomes = recebe_arquivo_nomes()
moda_nomes = busca_moda(nomes)
moda_sobrenomes = busca_moda(sobrenomes)
imprime_moda("Nome", moda_nomes, nomes)
imprime_moda("Sobrenome", moda_sobrenomes, sobrenomes)