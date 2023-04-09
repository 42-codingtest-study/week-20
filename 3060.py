#런타임에러

for _ in range(int(input)) :
    N = int(input)
    saryo = sum(list(map(int, input().split())))
    day = 1
    while N >= saryo :
        day += 1
        saryo *= 4
    print(day)