def recebe_pessoas():
    linha = input("Digite o nome das pessoas separados por virgula\n")
    linha = linha.split(",")
    pessoas = []
    for i in range(len(linha)):
        pessoas.append(linha[i])
    return pessoas

def cria_matriz_pessoa(lista):
    matriz_pessoas = []
    for pessoa in lista:
        idade = int(input(f"Digite a idade {pessoa}\n"))
        profissao = input(f"Digite a profissão de {pessoa}\n")
        estado = input(f"Digite o estado civil de {pessoa}\n")
        matriz_pessoas.append([idade, profissao, estado,pessoa])
    for pessoa in matriz_pessoas:
        print(pessoa)
    return matriz_pessoas

def media_idades(matriz):
    soma = 0
    for pessoa in matriz:
        soma+=pessoa[0]
    media=soma/len(matriz)
    return media

nome_pessoas = recebe_pessoas()
matriz_pessoas = cria_matriz_pessoa(nome_pessoas)
print(f"A média das idades é: {media_idades(matriz_pessoas)}")

