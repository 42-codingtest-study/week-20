#
# [level 1] 문자열 내 p와 y의 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/12916

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(s):
    p = 0
    y = 0

    for s in s.upper():
        if s == 'P': p += 1
        if s == 'Y': y += 1

    return True if p == y else False