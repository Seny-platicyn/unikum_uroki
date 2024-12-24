import random
weight = int(input())
height = int(input())
matrix = [[random.randint(1,10)for i in range(weight)] for j in range(height)]#
for row in matrix:
    for element in row:
        print(element, end='\t')#Ставит в конце таб
    print()#перенос строки