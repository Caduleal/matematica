def recebe_sequencia():
    sequencia = input().split()
    for i in range(len(sequencia)):
        sequencia[i] = int(sequencia[i])

    return sequencia

def cria_ciclos(sequencia):
    visitado = set()
    ciclos = []
    for i in range(len(sequencia)):
        if i+1 not in visitado:
            ciclo = []
            atual = i+1
            while atual not in visitado:
                visitado.add(atual)
                ciclo.append(atual)
                atual = sequencia[atual -1]
            ciclos.append(ciclo)
    return ciclos, len(ciclos)

sequencia = recebe_sequencia()
ciclos, quantidade = cria_ciclos(sequencia)
print(ciclos, quantidade)