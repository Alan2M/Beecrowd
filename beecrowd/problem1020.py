import os
os.system('cls')

dias = int(input())
anos = dias//365
meses = ((dias)-(anos*365))//30
dia = ((dias)-(anos*365))-30*meses
print(anos,"ano(s)")
print(meses,"mes(es)")
print(dia,"dia(s)")