#Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

def PrimeFact(n):
    res = []
    i = 2
    while i * i <=n:
        while n % i == 0:
            res.append(i)
            n = n / i
        i+=1
    if n > 1:
        res.append(int(n))
    return res

n = int(input('Введите натуральное число:'))
if n > 0:
    print(PrimeFact(n))
elif n < 0:
    print(PrimeFact(-n))
else:
    print('Введите число, отличное от нуля')