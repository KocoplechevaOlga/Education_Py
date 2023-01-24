# Напишите программу вычисления арифмитического выражения, заданного строкой.
# Используйте операции "+, -, /, *". приоритет операций стандартный.
# Добавте скобки, приоритет операций меняется

action = {
    "^": lambda x,y: str(float(x)**float(y)),
    "*": lambda x,y: str(float(x)*float(y)),
    "/": lambda x,y: str(float(x)/float(y)),
    "+": lambda x,y: str(float(x)+float(y)),
    "-": lambda x,y: str(float(x)-float(y))
}

def Calculetion(start_list):
    for i, val in enumerate(start_list):
        if isinstance(val, list):
            start_list[i] = Calculetion(val)
    t_list = [i for i, val in enumerate(start_list) if val in "*/"]
    while t_list:
        index_op = t_list[0]
        a, b, c = start_list[index_op-1:index_op+2]
        start_list.insert(index_op-1, action[b](a, c))
        del start_list[index_op:index_op+3]
        t_list = [i for i, val in enumerate(start_list) if val in "*/"]
    while len(start_list) > 1:
        a, b, c = start_list[:3]
        del start_list[:3]
        start_list.insert(0, action[b](a, c))
    return start_list[0]

def cut(list1):
    list2 = []
    i = 0
    while i < len(list1):
        if list1[i] == "(":
            fin = list1.index(")")
            list2.append(list1[i+1:fin])
            i = fin
        else:
            list2.append(list1[i])
        i +=1
    return list2


new_list = input('Введите выражение:').split()
l = cut(new_list)
print(Calculetion(l))