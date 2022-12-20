#Реализуйте алгоритм перемешивания списка.
#Без функции shuffle из модуля random.

from random import randint

l = int(input('ВВедите размер списка:'))
if l > 0:
    my_list = list(range(l))
    print(my_list)
    a = len(my_list)-1
    while a > 0:
        b = randint(0, a)
        my_list.append(my_list[b])
        my_list.pop(b)
        a-=1
    print(my_list)
else:
    print('Вы ввели не натуральное число, введите число больше 0')