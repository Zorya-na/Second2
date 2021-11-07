first = float(input())
second = float(input())
sign = input()
if sign == '+':
  print(first + second)
elif sign == "-":
  print(first - second)
elif sign == "/":
  if second == 0.0:
    print( "Деление на 0!" )
  else:
    print(first / second)
elif sign == "*":
  print(first * second)
elif sign == "mod":
  if second == 0.0:
    print( "Деление на 0!" )
  else:
    print(first % second)
elif sign == "pow":
  print(first ** second)
elif sign == "div":
  if second == 0.0:
    print( "Деление на 0!" )
  else:
    print(first // second)
    print(first // second)