'''Read 100 integer numbers. Print the highest read value and the input position.

Input
The input file contains 100 distinct positive integer numbers.

Output
Print the highest number read and the input position of this value, according to the given example.'''
import os
os.system('cls')

highest = 0
cont = 0
contH = 0
while cont<100:
    cont+=1
    num=int(input())
    if num>highest:
        highest = num
        contH = cont
print(highest)
print(contH)