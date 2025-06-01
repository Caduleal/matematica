def fibonacci():
    tempo = int(input())
    a=1
    b=2
    sequencia = [a,b]
    for i in range(3,tempo+1):
        aux = b
        b = a + b
        a = aux
        sequencia.append(b)
    ultimo_elemento = sequencia[tempo-1]
    print(f"O numero de casais de coelhos depois de {tempo} meses é {ultimo_elemento}")
    return sequencia

fibonacci()