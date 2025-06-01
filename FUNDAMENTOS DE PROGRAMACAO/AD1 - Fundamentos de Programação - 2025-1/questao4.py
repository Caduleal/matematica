def contar_substrings_distintas(k,s):
    letras_validas = {"A", "C", "G", "T"}

    s = s.upper()
    if any(letra not in letras_validas for letra in s):
        return "Sequência inválida"
    if k>len(s):
        return 0
    
    substrings_unicas = set()

    for i in range(len(s)-k+1):
        substrings_unicas.add(s[i:i+k])
    
    return len(substrings_unicas)

testes = [(3, "ACGACGTAG"), (4, "ACGXGTAG"), (2, "AATT"), (5, "ACGTACGT")]

for k, entrada in testes:
    print(contar_substrings_distintas(k, entrada))