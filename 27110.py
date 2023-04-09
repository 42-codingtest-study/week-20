N = int(input())
chi = list(map(int, input().split()))
res = 0

for i in range(3) :
    if chi[i] <= N :
        res += chi[i]
    else :
        res += N

print(res)