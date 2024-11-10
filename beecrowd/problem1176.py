import os
os.system('cls')

fib=[0,1]
n1=0
n2=1
T = int(input())

for i in range(60):
    fib_novo=n1+n2
    fib.append(fib_novo)
    n1=n2
    n2=fib_novo

for i in range(T):
    n = int(input())
    print(f"Fib({n}) =",fib[n])
