#
# [level 0] 짝수의 합
# https://school.programmers.co.kr/learn/courses/30/lessons/120831

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(n):
    sum = 0
    for i in range(2, n + 1):
        if i % 2 == 0:
            sum += i

    return sum