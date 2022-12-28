# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#    Напишите программу, которая определит, присутствует ли в заданном списке число,
#    полученное от пользователя.

from random import sample
def FindNumInList(count, num):
    my_list = sample(range(1, count*2), k=count)
    print(my_list)
    if num in my_list:
        return 'Yes'
    return 'No'

print(FindNumInList(int(input()), int(input())))
