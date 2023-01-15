#  Напишите программу, удаляющую из текста все слова, содержащие "абв". 
# В тексте используется разделитель пробел.
# Например:   in    Number of words: 10
#             out: авб абв бав абв вба бав вба абв абв абв
#                  авб бав вба бав вба

from random import choices

def CreatStrByWord(num, word):
    my_list = []
    for i in range(num):
        w = choices(word, k=3)
        my_list.append(''.join(w))
    str = (" ".join(my_list))
    return str

n = int(input('Введите размер списка:'))
if n > 0:
    star_word = input('Введите слово для формирования списка:')
    a = CreatStrByWord(n, star_word)
    print(a)
    del_word = input('Введите слово, для удвления из списка:')
    res = a.replace(del_word +' ', '')
    print(res)
else:
    print('Вы ввели некорректные данные. введите число больше 0')
