a = int(input())
b = int(input())
c = int(input())
min = a
max = a

if min <= b and min <= c:
    min = a
elif b <= min and b <= c:
    min = b
elif c <= min and c <= b:
    min = c

if max >= b and max >= c:
    max = a
elif b >= max and b >= c:
    max = b
elif c >= max and c >= a:
    max = c

other = (a + b + c) - (min + max)

print(max, '\n', min, '\n', other)