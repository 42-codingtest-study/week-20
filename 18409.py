n = int(input())
name = list(input())
result = 0

for i in range (0, n):
    if name[i] == 'a':
        result += 1
    elif name[i] == 'e':
        result += 1
    elif name[i] == 'i':
        result += 1
    elif name[i] == 'o':
        result += 1
    elif name[i] == 'u':
        result += 1

print(result)
