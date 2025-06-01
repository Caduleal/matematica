def verificar_dieta(n,casos):
    resultados = []

    for i in range(n):
        dieta = casos[i][0]
        cafe = casos[i][1]
        almoco = casos[i][2]

        trapaceou = False
        for alimento in cafe + almoco:
            if alimento not in dieta:
                trapaceou = True
                break

        if trapaceou:
            resultados.append("CHEATER")
        else:
            alimento_consumido = cafe + almoco
            jantar = "".join(sorted([alimento for alimento in dieta if alimento not in alimento_consumido]))
            resultados.append(jantar)

    return resultados

def main():
    n = int(input())
    casos = []


    for i in range(n):
        dieta=input().strip()
        cafe=input().strip()
        almoco=input().strip()
        casos.append((dieta,cafe,almoco))

        for resultado in verificar_dieta(n,casos):
            print(resultado)

main()