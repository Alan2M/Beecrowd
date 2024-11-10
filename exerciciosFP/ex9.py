import os
os.system('cls')

print("Digite [1] para sim e [0] para não")
vasc = int(input("Possui vascularização? "))
semen = int(input("Possui semente? "))
flor = int(input("Possui flores? "))

if vasc == 0 and semen == 0 and flor == 0:
    print("A planta é Bryophyta")
elif vasc == 1 and semen == 0 and flor == 0:
    print("A planta é Pteridophyta")
elif vasc == 1 and semen == 1 and flor == 0:
    print("A planta é Gymnospermae")
elif vasc == 1 and semen == 1 and flor == 1:
    print("A planta é Angiospermae")
else:
    print("Essa planta nem existe carai")