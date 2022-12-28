# Задайте строку из набора чисел. Напишите программу,
# которая покажет наибольшее и наименьшее число.
# в качестве разделител используйте пробел.

def UserInput(start_str):
    new_str = start_str.split()
    lst = []
    for i in range(len(new_str)):
        new_str[i] = new_str[i].strip(",.?/;:!=+")
        if new_str[i].replace('-', '', 1).isdigit():
            lst.append(new_str[i])
    return lst

def UserOutPut(lst):
    if lst:
        return min(lst, key = int), max(lst, key = int)
    return'Вы ввели некорректные данные'

print(UserOutPut(UserInput(input(""))))