X = int(input())
H = int(input())
M = int(input())
m = H * 60 + M
x = m + X
print(x // 60)
print(x % 60)