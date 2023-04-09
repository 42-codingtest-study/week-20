a, b, c = map(int, input().split())
d, e, f = map(int, input().split())

print(((d * 360 + (e - 1) * 30 + f) - (a * 360 + (b - 1) * 30 + c)) // 360)
print(d - a + 1)
print(d - a)