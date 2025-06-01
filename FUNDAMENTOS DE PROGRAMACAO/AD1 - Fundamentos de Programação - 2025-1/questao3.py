def complemento_reverso_dna(s):
    letras_validas={"A","C","G","T"}
    complemento = {"A":"T","T":"A","C":"G","G":"C"}

    s = s.upper()
    if any(letra not in letras_validas for letra in s):
        return "Sequência inválida"
    
    s_reverso = s[::-1]
    complemento_reverso="".join(complemento[letra] for letra in s_reverso)
    
    return f"Dada a sequência {s}, seu reverso complementar é: {complemento_reverso}" 


#Teste
entradas = ["acgctagctagc", "acgdctagas", "TGAC", "ccgatgcct"]
for entrada in entradas:
    print(complemento_reverso_dna(entrada))