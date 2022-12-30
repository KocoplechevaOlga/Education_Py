#Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной 
# последовательности в том же порядке.
# Например: in 7 ->  out [4, 5, 3, 3, 4, 1, 2] -> [5, 1, 2]

from random import sample
import random
def CreatRandomListByCount(count):
    my_list = []
    for i in range(count):
        my_list.append(random.randint(1, count))
    res = sample(my_list, count)
    return res
def FindSampleDigInList(lst):
    res = []
    for i in lst:
        if lst.count(i) == 1:
            res.append(i)
    return res

a = int(input('Введите размер списка:'))
if a > 0:
    list1 = CreatRandomListByCount(a)
    print(list1)
    print(FindSampleDigInList(list1))
else:
    print('Вы ввели некорректные данные, введите числа больше 0')