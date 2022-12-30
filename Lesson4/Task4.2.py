#Найдите корни квадратного уравнения c помощью модуля.
# запросите значения А, B, C 3 раза.
# Уравнения и модули запишите в файл

from math import sqrt
def Discrim(a, b, c):
    d = b**2-4*a*c
    with open ("File.txt", "a", encoding="utf-8") as my_File:
        my_File.write(f"{a}X2+{b}x+{c}=0\n")
        if d > 0 and a:
            x1 = round((-b + sqrt(d))/(2*a), 4)
            x2 = round((-b - sqrt(d))/(2*a), 4)
            my_File.write(f'Певый корень: {x1},\nВторой корень {x2}\n')
        elif d ==0 and a:
            x = round((-b/ (2*a)), 4)
            my_File.write(f'Корень: {x}\n')
        else:
            my_File.write('Решений нет\n')

for i in range(3):
    Discrim(int(input()),int(input()),int(input()))