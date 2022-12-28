# Задайте список, состоящий из произвольных слов, количество задаёт пользователь.
# Напишите программу, которая определит индекс второго вхождения строки в списке
# либо сообщит, что её нет.

from random import sample

def CreatListByWord(num, word = 'ABC'):
    my_list = []
    for i in range(num):
        w = sample(word, k=3)
        my_list.append(''.join(w))
    return my_list
def FindSeconWordInList(list1, word):
    if word in list1 and list1.count(word) > 1:
        index1 = list1.index(word)
        print(list1.index(word, index1+1))
    else:
        print('Значение на найдено')

new_list = CreatListByWord(int(input('введите размер списка: ')))
print(new_list)
FindSeconWordInList(new_list, input())
