def encontrar_sequencia(n,sequencia, numero_atual):
    if numero_atual == 0:
        print(sequencia)
        return 1
    
    total_sequencias = 0    
    for i in range(len(sequencia)- numero_atual-1):
        if sequencia[i] is None and sequencia[i+ numero_atual+1] is None:
            sequencia[i] = sequencia[i + numero_atual + 1] = numero_atual

            total_sequencias+= encontrar_sequencia(n,sequencia,numero_atual-1)

            sequencia[i] = sequencia[i + numero_atual+1] = None
    return total_sequencias

def gerar_sequencias(n):
    sequencia = [None]*(2*n)
    total = encontrar_sequencia(n,sequencia,n)

    if total == 0:
        print(f"Não há sequencias possíveis com o valor {n} de entradas")
    else:
        print(f"Há {total} sequências")

n = int(input())
gerar_sequencias(n)