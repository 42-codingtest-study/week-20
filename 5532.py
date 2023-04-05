L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

day_korean = 0
day_math = 0
if A % C == 0:
    day_korean += A // C
elif A % C != 0:
    day_korean += (A // C) + 1 

if B % D == 0:
    day_math += B // D
elif B % D != 0:
    day_math += (B // D) + 1

if day_korean >= day_math:
    print(L - day_korean)
else:
    print(L-day_math)