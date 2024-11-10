import os
os.system('cls')

par = 0
impar = 0
neg = 0
posit = 0

for i in range (5):
    n = int(input())
    if n%2==0:
        par+=1
    if n%2!=0:
        impar+=1
    if n>0:
        posit+=1
    if n<0:
        neg+=1
print(par, "valor(es) par(es)")
print(impar, "valor(es) impar(es)")
print(posit, "valor(es) positivo(s)")
print(neg, "valor(es) negativo(s)")