def recebe_pessoa():
    nomes = input("Digite os nomes ds pessoas, separados por virgula: ")
    nomes = nomes.split(",")
    matriz_pessoas = []

    for nome in nomes:
        crirar_matriz_pessoas(nome, matriz_pessoas)

    return matriz_pessoas


def crirar_matriz_pessoas(nome,matriz):
    idade = int(input(f"Digite a idade de {nome}:\n"))
    profissao = input(f"Digite a profissão de {nome}: \n")
    estado = input(f"Digite o estado civil de {nome}: \n")

    matriz.append([idade, profissao,estado,nome])

def imprime_matriz(matriz):
    print("\nMatriz de Pessoas:")
    for pessoa in matriz:
        print(pessoa)

    total_idades = sum(pessoa[0] for pessoa in matriz)
    media = total_idades / len(matriz)

    print(f"\nA média das idades é: {media:.2f}")


pessoas = recebe_pessoa()
imprime_matriz(pessoas)
