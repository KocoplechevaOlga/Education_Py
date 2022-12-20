#Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
#Без работы с методами строк.

def SumGigInFloutNon(a, n):
    if a < 0:
        a =a*(-1)
    b = int(a * (10**n))
    sum = 0
    while b // 10 > 0:
        sum = sum + b % 10
        b = b//10
    print(sum+b)

c = (input('введите число:'))
l = len(c)-1
c = float(c)
SumGigInFloutNon(c, l)
