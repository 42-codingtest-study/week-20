#
# [level 0] 외계행성의 나이
# https://school.programmers.co.kr/learn/courses/30/lessons/120834

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(age):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    x = list(map(int, str(age)))
    y = []

    for i in x:
        y.append(alpha[i])

    return ''.join(y)