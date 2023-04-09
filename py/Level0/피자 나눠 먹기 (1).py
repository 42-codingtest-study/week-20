#
# [level 0] 피자 나눠 먹기 (1)
# https://school.programmers.co.kr/learn/courses/30/lessons/120814

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(n):
    if n % 7 != 0:
        return n // 7 + 1
    else:
        return n // 7