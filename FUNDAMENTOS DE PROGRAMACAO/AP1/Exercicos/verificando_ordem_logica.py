def recebe_lista():
    linha = input()
    valores = []
    while linha != "":
        numeros = linha.split()
        for i in range(len(numeros)):
            valores.append(int(numeros[i]))
        linha = input()
    return valores

def verifica_ordem(lista):
    encontrou = False
    for i in range(len(lista)-10):
        print(f"Comparando lista[{i}] = {lista[i]} com lista[{i+10}] = {lista[i+10]}")
        if lista[i]==lista[i+10]:
            print(f"🔹 Condição satisfeita: lista[{i}] == lista[{i+10}] == {lista[i]}")
            encontrou= True
        return encontrou
def main():
    numeros = recebe_lista()
    if verifica_ordem(numeros):
        print("A condição é verdadeira!")
        print(numeros)
    else:
        print("A lista não satisfaz a condição")
        
main()
