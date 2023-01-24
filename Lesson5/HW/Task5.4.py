#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

from itertools import groupby, starmap
from os import path

def RLEEncode(text = "text_words.txt", code_text = "text_code_words.txt"):
    if path.exists(text):
        with open (text) as my_file1, \
                open (code_text, "a") as my_file2:
            for i in my_file1:
                my_file2.write("".join([f"{len(list(v))}{ch}" for ch, v in groupby(i)]))
    else:
        print("Файл не найден")

def RleDecode (start_file):
    if path.exists(start_file):
        with open(start_file) as my_file:
            n = ""
            for i in my_file:
                word_num = []
                for j in i.strip():
                    if j.isdigit():
                        n += j
                    else:
                        word_num.append([int(n), j])
                        n = ""
                print("".join(starmap(lambda x, y: x*y, word_num)))
    else:
        print("Файл не найден")

#RLEEncode(input("Введиет название файла: "), input("Введите название файла для записи: ")
#RleDecode(input("Введите названия файла для деклдирования: "))
RLEEncode()
RleDecode(input("Введите названия файла для деклдирования: "))
