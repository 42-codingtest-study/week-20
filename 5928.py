a, b, c = map(int, input().split())

n1 = a * 24 * 60 + b * 60 + c
n2 = 11 * 24 * 60 + 11 * 60 + 11

s = n1 - n2

if s < 0 :
    print(-1)
else :
    print(s)