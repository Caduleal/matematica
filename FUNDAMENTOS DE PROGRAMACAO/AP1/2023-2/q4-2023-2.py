def subir_escada(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    a=1
    b=2
    lista = [a,b]
    for i in range(3,n+1):
        aux = b
        b = a +b
        a = aux
        lista.append(b)

    return lista[n-1]

n= int(input())
print(f"Posso subir a escada de {n} degraus de {subir_escada(n)} maneiras")

    