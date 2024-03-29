#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# Например:  in  88 -> out  1011000
#            in  11 -> out 1011

def ConvertToBin(num: int):
    res = list()
    while num  > 0:
        res.insert(0, num%2)
        num //=2
    return res

a = int(input('Введите натуральное число:'))
b = ConvertToBin(a)
print(f"{a} в двоичной системе составляет:")
print(*b, end="")