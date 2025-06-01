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

    
#Teste
entrada = "acgctasdagctwqa"
print(verificar_sequencia_dna(entrada))
