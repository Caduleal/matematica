n = int(input())
valores_in = []
valores_out = []
for _ in range(n):
    valor = float(input())
    if valor >=10 and valor <=20:
        valores_in.append(valor)
    else:
        valores_out.append(valor)
    
print(f"{len(valores_in)} in")
print(f"{len(valores_out)} out")