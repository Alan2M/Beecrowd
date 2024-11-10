import os
os.system('cls')

v = []
n = int(input())
for i in range (10):
    v.append(n)
    n = n*2
    
    print(f"N[{i}] = {v[i]}")