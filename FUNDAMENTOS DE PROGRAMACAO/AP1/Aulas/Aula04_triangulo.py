def pode_formar_triangulo(a,b,c):
    return a+b> c and a+c > b and b+c > a

def verificar_quatro_varetas(a,b,c,d):
    if (pode_formar_triangulo(a,b,c) or
        pode_formar_triangulo(a,b,d) or
        pode_formar_triangulo(a,c,d) or
        pode_formar_triangulo(b,c,d)):
        return "S"
    return "N"

valores = input()
valores = valores.split()
for i in range(len(valores)):
    valores[i] = int(valores[i])    

print(verificar_quatro_varetas(*valores))
