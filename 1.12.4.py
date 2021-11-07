name = input()
if name == "треугольник":
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c)/2
    S = float((p * (p - a) * (p - b) * (p - c)) ** 0.5)
elif name == "прямоугольник":
    a = int(input())
    b = int(input())
    S = float(a * b)
else:
    pi = 3.14
    r = int(input())
    S = float(pi * r ** 2)
print(S)