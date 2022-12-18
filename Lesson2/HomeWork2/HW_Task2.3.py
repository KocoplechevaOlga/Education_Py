#Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# for 6: [2.0, 2.25, 2.37, 2.441, 2.488, 2.522], Sum = 14.071

def CreatListByFunc(l, num):
    c = 1
    while len(l) < num:
        l.append(round((1 + 1/c)**c, 3))
        c+=1
    return l

n = int(input('Введите натуральное число:'))
my_list = list()
print((CreatListByFunc(my_list, n)))
print(sum(CreatListByFunc(my_list, n)))
