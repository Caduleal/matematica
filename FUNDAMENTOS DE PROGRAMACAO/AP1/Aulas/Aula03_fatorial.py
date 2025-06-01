n = int(input())
while n <=0 or n>=13:
    n = int(input())
fatorial=1
for i in range(n,1,-1):
    fatorial = fatorial*i

print(fatorial)