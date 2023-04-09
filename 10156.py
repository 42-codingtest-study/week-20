k, n, m = map(int,input().split())
need = 0
price = k * n

if price < m:
    print(0)
else:
    need = (price - m)
    print(abs(need))