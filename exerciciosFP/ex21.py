import os
os.system('cls')

notas = []
for i in range(5):
    notas.append(int(input("Digite as notas:")))
media = sum(notas)/len(notas)
print("A media da turma é:",media)
for notas in notas:
    if notas > media:
        print(notas)