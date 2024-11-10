import os
os.system('cls')

def media(a,b):
    m = (a+b)/2
    return m

def imc(h,k):
    imc = k/h**2
    return imc
    
altura = float(input())
peso = float(input())
print(media(altura,peso))
print(imc(altura,peso))
