import math

print("Введите стороны треугольника")
print("Сторона a:")
a=float(input())
print("Сторона b:")
b=float(input())
print("Сторона с:")
c=float(input())
p = a + b + c
print("Периметр: ", p)
p /= 2
s = math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Площадь: ", s)