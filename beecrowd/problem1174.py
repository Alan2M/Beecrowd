import os
os.system('cls')

A = []
for i in range (100):
    n = float(input())
    A.append(n)
    if A[i] <= 10:
        print(f"A[{i}] = {A[i]:.1f}")
