def verificar_sequencia_dna(s):
    letras_validas =  {"A", "C","G","T"}
    posicoes_invalidas=[]

    for i in range(len(s)):
        if s[i].upper() not in letras_validas:
            posicoes_invalidas.append(i)
    
    if posicoes_invalidas:
        if len(posicoes_invalidas) == 1:
            return f"Sequência inválida, pois na posição {posicoes_invalidas[0]} o elemento não possui valor esperado"
        else:
            return f"Sequência inválida, pois nas posições {posicoes_invalidas} os elementos não possuem valores esperados"

    contagem = {base: s.upper().count(base) for base in letras_validas}

    return (
        f"Sequência válida. Além disso, a contagem de cada base nitrogenada é: "
        f"A: {contagem['A']} C: {contagem['C']} G: {contagem['G']} T: {contagem['T']}"
    )

#Teste
entrada = "ccgatgccta"
print(verificar_sequencia_dna(entrada))
