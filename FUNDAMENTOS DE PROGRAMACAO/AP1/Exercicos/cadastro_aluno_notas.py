def recebe_alunos():
    alunos = []
    linha = input()
    while linha != "":
        alunos.append(linha)
        linha = input()
    return alunos

def recebe_notas(alunos):
    matriz_notas = []
    for aluno in alunos:
            nota = input(f"Digite as notas do aluno {aluno} separados por ' ':").split()
            while len(nota) != 3:
                nota = input(f"Digite as notas do aluno {aluno} separados por ' ':").split()   
            for j in range(len(nota)):
                nota[j]= float(nota[j])
            matriz_notas.append([aluno]+nota)
    return matriz_notas

def calcula_media(boletim):
    for aluno in boletim:
        nome = aluno[0]
        notas = aluno[1:]
        media = sum(notas)/len(notas)
        status = "Aprovado" if media >= 6 else "Reprovado"
        print(f"{nome}: Média: {media:.2f} - {status}")

nomes_alunos = recebe_alunos()
matriz_aluno_nota=recebe_notas(nomes_alunos)
calcula_media(matriz_aluno_nota)

        

