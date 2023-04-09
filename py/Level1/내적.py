#
# [level 1] 내적
# https://school.programmers.co.kr/learn/courses/30/lessons/70128

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(a, b):
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]

    return result