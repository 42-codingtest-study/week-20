t = int(input())

for _ in range (0, t) :
    feed_max = int(input())
    pigs = list(map(int, input().split()))
    answer = 1
    eat = 0
    for j in pigs :
            eat += j
    while(True) : 
        if eat > feed_max :
            print(answer)
            break
        else :
            eat *= 4
            answer += 1