valores = input()
numeros = []
for valor in valores.split():
    numeros.append(int(valor))


for numero in numeros:
    print(numero)

for i in range(0,len(numeros)-1):
    if numeros[i] > numeros[i+1]:
        auxiliar = numeros[i]
        numeros[i] = numeros[i+1]
        numeros[i+1] = auxiliar

for numero in numeros:
    print(numero)