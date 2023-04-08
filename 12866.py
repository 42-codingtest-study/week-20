l = int(input())
s = list(input())

a, c, g, t = 0, 0, 0, 0

for i in range(0, l) :
    if s[i] == 'A':
        a += 1
    elif s[i] == 'C':
        c += 1
    elif s[i] == 'G':
        g += 1
    elif s[i] == 'T':
        t += 1
        
print((a*c*g*t) % 1000000007)