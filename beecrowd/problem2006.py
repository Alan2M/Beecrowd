import os
os.system('cls')

soma = 0
i = int(input())
while i < 1 and i > 4:
    i = int(input())
for n in range(5):
    resp = int(input())
    if resp == i:
        soma+=1
print(soma)