#
# [level 0] 소인수분해
# https://school.programmers.co.kr/learn/courses/30/lessons/120852

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(n):
    answer = []

    x = 2
    while x <= n:
        if n % x == 0:
            if x not in answer:
                answer.append(x)
            n //= x
        else:
            x += 1

    return answer