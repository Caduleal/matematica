n = int(input())
while n >1000000:
    n= int(float())

Notas100 = n//100
notas = n % 100

notas50 = n // 50
n = n % 50 

notas20 = n // 20
n = n % 20 

notas10 = n // 10
n = n % 10

notas05 = n // 5
n = n % 5

notas02= n//2
n = n % 2

notas01 = n//1


print(f"{Notas100} nota(s) de R$ 100")
print(f"{notas50} nota(s) de R$ 50")
print(f"{notas20} nota(s) de R$ 20")
print(f"{notas10} nota(s) de R$ 10")
print(f"{notas05} nota(s) de R$ 5")
print(f"{notas02} nota(s) de R$ 2")
print(f"{notas01} nota(s) de R$ 1")