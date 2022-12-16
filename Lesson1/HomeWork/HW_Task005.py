#Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

def FindDistByCoordIn2D(x, y, w, z):
    dist = round(((x-w)**2+(y-z)**2)**0.5, 2)
    print(dist)

print('Введите координаты первой точки:')
a = float(input('X1 = '))
b = float(input('Y1 = '))
print('Введите координаты второй точки:')
c = float(input('X2 = '))
d = float(input('Y2 = '))

FindDistByCoordIn2D(a, b, c, d)