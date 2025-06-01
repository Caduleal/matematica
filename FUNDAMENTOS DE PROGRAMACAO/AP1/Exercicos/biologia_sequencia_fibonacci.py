def sequencia_fibonacci(n):
    a = 1
    b = 2
    sequencia = [a,b]
    for i in range(2,n):
        sequencia.append(sequencia[i-1]+sequencia[i-2])
    return sequencia

n = int(input())
print(sequencia_fibonacci(n))
        