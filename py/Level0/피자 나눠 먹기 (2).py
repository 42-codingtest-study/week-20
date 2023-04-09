#
# [level 0] 피자 나눠 먹기 (2)
# https://school.programmers.co.kr/learn/courses/30/lessons/120815

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(n):
    for i in range(1, 100):
        if (i * 6) % n == 0:
            return i