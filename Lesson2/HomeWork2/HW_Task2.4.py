#Напишите программу, которая принимает на вход 2 числа.
#Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
#Найдите произведение элементов на указанных позициях(не индексах).

def CreatListByNegToPositivNum(num):
    l = [-num]
    c = 0
    while c < num*2:
        l.append((l[c] + 1))
        c+=1
    return l

n = int(input('Введите натуральное число:'))
list1 = CreatListByNegToPositivNum(n)
print(list1)
a = int(input('Ведите позицию первого числа:'))
b = int(input('Ведите позицию второго числа:'))
if 0 <= a <= len(list1) and 0 <= b <= len(list1):
    print(list1[a-1] * list1[b-1])
else:
    print('Таких позиций в заданном списке нет')