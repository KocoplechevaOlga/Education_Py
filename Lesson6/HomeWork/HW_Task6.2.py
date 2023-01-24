#Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
#Например: in 424 ->  out [20, 21, 40, 42, 60, 63, 80, 84, 100, 105, 120, 126, 140, 147, 
#                           160, 168, 180, 189, 200, 210, 220, 231, 240, 252, 260, 273, 280, 
#                           294, 300, 315, 320, 336, 340, 357, 360, 378, 380, 399, 400, 420]


def CreatRangeListByCount(count):
    my_list = [i for i in range(20, count+1)]
    return my_list

l = int(input("Введите натуральное число:"))
if l > 20:
    my_list = CreatRangeListByCount(l)
    res_list = [int(i) for i in my_list if i % 20 == 0 or i % 21 == 0]
    print(res_list)