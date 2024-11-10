import os
os.system('cls')

A = []
B = []
C = []

for i in range(10):
    n = int(input("Digite valor do vetor A:\n"))
    A.append(n)
for i in range(10):
    if A[i]%2 == 0:
        B.append(A[i])
    else:
        C.append(A[i])
print(A)
print(B)
print(C)