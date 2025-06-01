def processa_nome(lista_nome):
    parte_nome = lista_nome.split()
    print(parte_nome[0],parte_nome[len(parte_nome)-1])
    return None


qtd_nomes = int(input())
for i in range(qtd_nomes):
    nomeCompleto= input()
    processa_nome(nomeCompleto)

    