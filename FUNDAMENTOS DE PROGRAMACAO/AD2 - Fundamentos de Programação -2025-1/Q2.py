def verifica_arquivo_palindromo(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        posicoes = []
        while True:
            pos = f.tell()
            linha = f.readline()
            if not linha:
                break
            posicoes.append(pos)

    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        linhas_normais = []
        for pos in posicoes:
            f.seek(pos)
            linhas_normais.append(f.readline().strip())


        linhas_invertidas = []
        for pos in reversed(posicoes):
            f.seek(pos)
            linhas_invertidas.append(f.readline().strip())

    return linhas_normais==linhas_invertidas

def main():
    nome_arquivo = input("Digite o nome do arquivo: ")
    if verifica_arquivo_palindromo(nome_arquivo):
        print(f"O arquivo é palindromo linha a linha")
    else:
        print("O arquivo não é palindromo linha a linha")

main()

    
        