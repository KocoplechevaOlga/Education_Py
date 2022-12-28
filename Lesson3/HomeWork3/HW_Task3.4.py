#Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
#Напишите программу, которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.
#Например:  in 5 ->  out [5.16, 8.62, 6.57, 7.92, 9.22], Min: 0.16, Max: 0.92. Difference: 0.76

from random import uniform
def CreatRandomListByCount(count:int):
    my_list = []
    if count <= 0:
        print('Пазмер списка не может быть отрицательным числом. введите число больше 0')
        return[0.0]
  
    for i in range(count):
        my_list.append(round(uniform(1, count), 2))
    return my_list

def DifMinAndMaxInList(start_list):
    nMin = nMax = start_list[0] % 1
    for i in range(1, len(start_list)):
        elem = round(start_list[i] % 1, 2)
        if elem > nMax:
            nMax = elem
        elif elem < nMin:
            nMin = elem
    res = round(nMax-nMin, 2)
    print(f"Min:{nMin:.2f}, Max:{nMax:.2f}. Разница между максисмальны и минимальным:{res}")
    return res

new_list = CreatRandomListByCount(int(input('Введите размер списка:')))
print(new_list)
DifMinAndMaxInList(new_list)