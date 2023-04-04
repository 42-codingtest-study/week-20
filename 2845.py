a, b = list(map(int, input().split()))
p = list(map(int, input().split()))

max = a * b
for i in p:
    print(i - max, end = " ")