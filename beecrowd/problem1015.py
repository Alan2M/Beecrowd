import os
os.system('cls')

x1,y1 = input().split()
x2,y2 = input().split()
x1 = float(x1)
x2 = float(x2)
y1 = float(y1)
y2 = float(y2)
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("%.4f"%distance)