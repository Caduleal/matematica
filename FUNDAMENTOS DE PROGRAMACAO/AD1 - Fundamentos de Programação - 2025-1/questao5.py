from collections import defaultdict

def encontrar_substrings(k, n, s):
    letras_validas = {"A", "C", "G", "T"}

    s = s.upper()
    if any(letra not in letras_validas for letra in s):
        return "Sequência inválida"

    if k > len(s):
        return ""

    contagem_substrings = defaultdict(int)

    for i in range(len(s) - k + 1):
        substring = s[i:i+k]
        contagem_substrings[substring] += 1 

    substrings_repetidas = [sub for sub, count in contagem_substrings.items() if count >= n]

    return "\n".join(substrings_repetidas) if substrings_repetidas else ""

# Teste
entradas = [
    (3, 2, "ACGACGTAGACG"),
    (3, 2, "ACGXGTAG"),  
    (2, 2, "AATT"),  
    (4, 2, "ACGTACGT"),  
]

for k, n, s in entradas:
    print(encontrar_substrings(k, n, s))
