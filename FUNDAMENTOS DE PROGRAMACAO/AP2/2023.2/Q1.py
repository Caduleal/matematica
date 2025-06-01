def le_arquivo_float(arquivo):
    with open(arquivo, 'r') as fin:
        print(f"Conteúdo em {arquivo}: ")
        for linha in fin:
            print(linha,end="")
    return None

def calcula_media(arquivo):
    with open(arquivo, 'r') as fin:
        soma = 0
        total = 0
        for linha in fin:
            numeros =linha.strip("\n").split()
            for numero in numeros:
                soma+=(float(numero))
                total+=1
        media=soma/total
    return media

def imprime_resultado(arquivo):
    media = calcula_media(arquivo)
    qtd_acima_media = 0
    with open(arquivo, 'r') as fin:
        for linha in fin:
            numeros = linha.strip("\n").split()
            for numero in numeros:
                if float(numero) > media:
                    qtd_acima_media +=1
    print(f"\nMédia dos numeros em {arquivo}: {media}")
    print(f"Quantidade acima de {media} em {arquivo}: {qtd_acima_media}")
    return None

def main():
    nome_arquivo = input()
    le_arquivo_float(nome_arquivo)
    imprime_resultado(nome_arquivo)

main()

