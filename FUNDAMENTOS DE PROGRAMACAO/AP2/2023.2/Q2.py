def le_arquivo(arquivo):
    with open(arquivo,'r', encoding="utf-8") as fin:
        print(f"Conteúdo do arquivo {arquivo}")
        for linha in fin:
            print(linha, end="")
    return None
    
def cria_dicionario_palavra_tamanho(arquivo):
    dic_palavras = dict()
    with open(arquivo, 'r', encoding="utf-8") as fin:
        num_linha =1
        for linha in fin:
            palavras = linha.strip('\n').split()
            for palavra in palavras:
                if palavra in dic_palavras:
                    if num_linha not in dic_palavras[palavra][1]:
                        dic_palavras[palavra][1].append(num_linha)
                else:
                    dic_palavras[palavra]=[len(palavra),[num_linha]]
            num_linha+=1
    return dic_palavras

def imprime_maior_palavra(arquivo):
    dicionario = cria_dicionario_palavra_tamanho(arquivo)
    lista = list(dicionario.items())
    lista_ordenada = sorted(lista, key=lambda x:x[1][0], reverse=True)
    palavra_mais_longa = lista_ordenada[0][0]
    tamanho = lista_ordenada[0][1][0]
    linhas = lista_ordenada[0][1][1]
    print(f"Palavra de maior comprimento: {palavra_mais_longa}")
    print(f"Qual(is) linha(s) ocorreu: {linhas}")
    return None

def main():
    nome_arquivo = input()
    le_arquivo(nome_arquivo)
    imprime_maior_palavra(nome_arquivo)
    return None
main()

