def recebe_letras():
    linha = input().strip().split()
    letras = []
    for i in range(len(linha)):
        letras.append(linha[i])
    return letras

def cria_combinação(letras, n):
    if n == 0:
        return ['']
    palavras_anteriores = cria_combinação(letras, n-1)
    novas_palavras = []

    for palavas in palavras_anteriores:
        for letra in letras:
            novas_palavras.append(palavas+letra)

    for i in range(len(novas_palavras)):
        print(f'"{novas_palavras[i]}",',end=" ")
    return novas_palavras

letras_iniciais = recebe_letras()
tamanho = len(letras_iniciais)
cria_combinação(letras_iniciais, tamanho)
