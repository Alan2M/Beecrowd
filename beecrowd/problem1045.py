import os
os.system('cls')

def triangulo(a,b,c):
    resp = []
    if a >= b+c or b >= a+c or c >= b+a:
        resp.append("NÃO FORMA TRIANGULO")
        return
    if a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b:
        resp.append("TRIANGULO RETANGULO")
    elif a*a > b*b + c*c or b*b > c*c + a*a or c*c > a*a + b*b:
        resp.append("TRIANGULO OBTUSANGULO")
    elif a*a < b*b + c*c or b*b < c*c + a*a or c*c < a*a + b*b:
        resp.append("TRIANGULO ACUTANGULO")
    if a==b==c:
        resp.append("TRIANGULO EQUILATERO")
    elif a==b or a==c or b==c:
        resp.append("TRIANGULO ISOSCELES")
    return resp

l1,l2,l3 = map(float, input().strip().split())
resultado = triangulo(l1,l2,l3)
for r in resultado:
    print(r)