# Создайте список из N натуральных чисел, упорядоченных по возрастанию. 
#Среди чисел не хватает одного, что бы выполняллось условие А[i-1] = A[i]-1. Найдите это число

from random import choice

def CreateList(n):
    ls = [i for i in range(n+1)]
    ls.remove(choice(ls))
    return ls

def FindNum (lst):
    for i in range(1, len(lst)):
        if lst[i]-1 != lst[i-1]:
            return lst[i]-1
    return -1

a = int(input('Введите натуральное число:'))
if a > 0:
    new_list = CreateList(a)
    print(new_list)
else:
    print('Введите число больше 0')

print(f"Искомое число: {FindNum(new_list)}")