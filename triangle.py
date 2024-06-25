import math

print("Введите стороны треугольника")
print("АВ:")
ab=float(input())
print("BC:")
bc=float(input())
print("CA:")
ca=float(input())
p = ab + bc + ca
print("Периметр: ", p)
p/=2
s = math.sqrt(p*(p-ab)*(p-bc)*(p-ca))
print("Площадь: ", s)