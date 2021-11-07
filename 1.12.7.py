a = input()
a = int(a)

left = a // 1000
right = a % 1000

first = left // 100
second = left // 10 % 10
third = left % 10

fourth = right // 100
fifth = right // 10 % 10
sixth = right % 10

if (first + second + third) == (fourth + fifth + sixth):
  print("Счастливый")
else:
  print("Обычный")