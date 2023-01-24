# Представлен список чисел. Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента. Use comprehension.
# Например: in 9  ->  out [15, 16, 2, 3, 1, 7, 5, 4, 10]
#                           [16, 3, 7, 10]

from random import sample

def CreatRandomListByCount(count):
    my_list = sample(range(1, count*3), k=count)
    return my_list

l = int(input('Введите размер списка:'))
if l > 0:
    my_list = CreatRandomListByCount(l)
    print(my_list)
    res_list = [int(i) for i in my_list[1:l] if i > my_list[my_list.index(i)-1]]
    print(res_list)
else:
    print('Вы ввели некорректный размер списка, введите число больше 0')