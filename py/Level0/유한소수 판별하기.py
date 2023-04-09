#
# [level 0] 유한소수 판별하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120878

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(a, b):
    for i in range(2, min(a, b) + 1):
        if (a % i == 0 and b % i == 0):
            a = a // i
            b = b // i

    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5

    return 1 if b == 1 else 2  # 다 나누어 떨어지면 1,아니면 2넣기


from math import gcd


def solution(a, b):
    b //= gcd(a, b)

    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5

    return 1 if b == 1 else 2  # 다 나누어 떨어지면 1,아니면 2넣기