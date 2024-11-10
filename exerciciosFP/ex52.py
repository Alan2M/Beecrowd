import os
os.system('cls')

file = open("arquivo1.txt", "w", encoding="utf8")

for i in range (5):
    n = str(input())
    file.write(n)
file.close()
file = open("arquivo1.txt", "r", encoding="utf8")
print(file.read())