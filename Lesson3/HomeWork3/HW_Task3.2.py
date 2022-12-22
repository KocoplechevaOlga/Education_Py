#Напишите программу, которая найдёт произведение пар чисел списка.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Например: in 4 -> out [2, 5, 8, 10] -> [20, 40];
#           in 5 -> out [2, 2, 4, 8, 8] -> [16, 16, 4]

from random import sample
def CreatRandomListByCount(count, n):
    my_list = sample(range(1, count*n), k=count)
    return my_list
def CreatNewListFromMultElemInList(start_list):
    res = list()
    l = len(start_list)
    for i in start_list:
        res.append(i*start_list[l-1])
        l-=1
        if l < ((len(start_list)/2)+1):
            break
    if len(start_list) % 2 == 0:
        return res
    else:
        res.append(start_list[l-1])
        return res

a = int(input('Введите размер списка:'))
b = int(input('введите уровень ограничения:'))
if a > 0 and b > 0:
    list1 = CreatRandomListByCount(a, b)
    print(list1)
else:
    print('Вы ввели некорректные данные, введите числа больше 0')
print(CreatNewListFromMultElemInList(list1))
