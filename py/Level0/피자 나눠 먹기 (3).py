#
# [level 0] 피자 나눠 먹기 (3)
# https://school.programmers.co.kr/learn/courses/30/lessons/120816

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(slice, n):
    if n % slice != 0:
        return n // slice + 1
    else:
        return n // slice