import sys

num = sys.stdin.readline

n, m = map(int,num().split())
A, B = "",""

for _ in range(n):
    for i in num().rstrip():
        A += i * 2
        
for _ in range(n):
    B += num().rstrip()

if A == B :
    print('Eyfa')
else :
    print('Not Eyfa')