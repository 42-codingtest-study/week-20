#
# [level 0] 팩토리얼
# https://school.programmers.co.kr/learn/courses/30/lessons/120848

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(n):
    for i in range(n):
        if n < factorial(i):
            return i - 1

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result