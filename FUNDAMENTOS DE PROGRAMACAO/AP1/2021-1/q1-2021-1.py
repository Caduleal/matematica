def maneira_subir():
    n=int(input())
    a=1
    b=2
    sequencia = [a,b]
    for i in range(3,n+1):
        aux = b
        b=a+b
        a=aux
        sequencia.append(b)
    print(f"Posso subir a escada de {n} degraus de {sequencia[n-1]}")
    return None
maneira_subir()

