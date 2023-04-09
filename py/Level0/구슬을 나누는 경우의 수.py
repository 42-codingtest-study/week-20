#
# [level 0] 구슬을 나누는 경우의 수
# https://school.programmers.co.kr/learn/courses/30/lessons/120840

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(balls, share):
    return facto(balls) / (facto(balls - share) * facto(share))


def facto(n):
    answer = 1

    for i in range(2, n + 1):
        answer *= i

    return answer