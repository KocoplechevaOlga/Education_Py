# Создайте спискок, в который поажают числа, описывающие
# возрастающую последовательность. Порядок элементов менять нельзя

from random import choices

def SertNums (ls):
    n = []
    for i in range(len(ls)):
        t = ls[i]
        t_list = [t]
        for j in range(i+1, len(ls)):
            if ls[j] > t:
                t = ls[j]
                t_list.append(t)
        if len(t_list) > 1:
            n.append(t_list)
    return n

n = int(input('Введите целое число:'))
if n > 0:
    my_list = choices(range(n*3), k = n)
    print(my_list)
    print(SertNums(my_list))
else:
    print('Введите число больше 0')