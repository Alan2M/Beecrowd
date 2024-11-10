import os
os.system('cls')

banho = 0
tosa = 0
banhotosa = 0
outros = 0
for i in range(5):
    resposta = int(input("1 - banho\n2 - tosa\n3 - banho e tosa\n4 - outros\n"))
    if resposta == 1:
        banho+=1
    elif resposta == 2:
        tosa+=1
    elif resposta == 3:
        banhotosa+=1
    elif resposta == 4:
        outros+=1
print("banho:",banho)
print("tosa:",tosa)
print("banho e tosa:",banhotosa)
print("outros:",outros)