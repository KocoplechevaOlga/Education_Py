#Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# Например:   in   5   -> out  [10, 2, 3, 8, 9]  sum = 22

from random import sample
def CreatRandomListByCount(count):
    my_list = sample(range(1, count*2), k=count)
    return my_list

new_list = CreatRandomListByCount(int(input('Введите размер списка:')))
print(new_list)
print(f"Ссума элементов, стоящих на нечетных позициях равна: {sum(new_list[::2])}")
