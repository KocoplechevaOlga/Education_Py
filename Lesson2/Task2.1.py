# Напиште прогамму, которая на вход принимает число N
# и выдвет последовательность N чисел 
# например: N = 5  -> 1, -3, 9, -27, 81

def nFunc (num):
    for i in range(num):
        print((-3)**i, end = ' ')

n = int(input('Введите натуральное число:'))
nFunc(n)