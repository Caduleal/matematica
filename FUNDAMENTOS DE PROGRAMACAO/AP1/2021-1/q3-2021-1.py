def recebe_letras():
    linha = input().strip().split()
    letras = []
    for i in range(len(linha)):
        letras.append(linha[i])
    return letras, len(letras)

def gera_palavras(letras, tamanho):
    if tamanho ==0:
        return ['']
    palavras_anteriores = gera_palavras(letras, tamanho-1)
    novas_palavras = []

    for palavra in palavras_anteriores:
        for letra in letras:
            novas_palavras.append(palavra+letra)
    
    for i in range(len(novas_palavras)):
        print(f'"{novas_palavras[i]}",',end=" ")
    return novas_palavras
    
base_letras, tamanho = recebe_letras()
gera_palavras(base_letras,tamanho)
