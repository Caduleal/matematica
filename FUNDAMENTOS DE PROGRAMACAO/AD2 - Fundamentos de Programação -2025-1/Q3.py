def limpar_palavra(palavra):
    nova_palavra = ''
    for caractere in palavra:
        if caractere.isalnum():
            nova_palavra+= caractere.lower()
    return nova_palavra

def contar_palavras(nome_arquivo):
    contagem = {}
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            palavras = linha.strip().split()
            for palavra in palavras:
                palavra_limpa = limpar_palavra(palavra)
                if palavra_limpa != "":
                    if palavra_limpa in contagem:
                        contagem[palavra_limpa]+=1
                    else:
                        contagem[palavra_limpa] =1
    return contagem

def ordenar_por_frequencia(contagem):
    lista_ordenada = []
    for palavra in contagem:
        lista_ordenada.append((palavra, contagem[palavra]))

    for i in range(len(lista_ordenada)):
        for j in range(i+1,len(lista_ordenada)):
            if lista_ordenada[i][1] < lista_ordenada[j][1]:
                lista_ordenada[i], lista_ordenada[j] = lista_ordenada[j], lista_ordenada[i]
            
    return lista_ordenada
    
def main():
    nome_arquivo = input("Digite o nome do arquivo: ")
    contagem = contar_palavras(nome_arquivo)
    ordenadas = ordenar_por_frequencia(contagem)

    for palavra, frequencia in ordenadas:
        print(f"{palavra} : {frequencia}")


main()
