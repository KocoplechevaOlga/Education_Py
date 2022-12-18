# Напишите программу, которая принимает на вход число N
#и выдает набор произведений чисел от 1 до N в виде списка.

#1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
#- 4 -> [1, 2, 6, 24]
#- 6 -> [1, 2, 6, 24, 120, 720]

def CreatListBuMiltNum(l, num):
    if num == 1:
        l.pop(1)
        return l
    elif num == 2:
        return l
    else:
        c = len(l)
        while c < num:
            l.append((c+1) * l[c-1])
            c +=1
        return l

my_List = [1, 2]
n = int(input('Введите натуральное число:'))
if n >= 0:
    res = CreatListBuMiltNum(my_List, n)
    print(res)
else:
    print('Ведите число, больше 0')