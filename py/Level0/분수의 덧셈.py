#
# [level 0] 분수의 덧셈
# https://school.programmers.co.kr/learn/courses/30/lessons/120808

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(numer1, denom1, numer2, denom2):
    # 분자
    numer = numer1 * denom2 + numer2 * denom1
    # 분모
    denom = denom1 * denom2

    max = 1
    for i in range(2, denom + 1):
        if numer % i == 0 and denom % i == 0:
            max = i

    return [numer / max, denom / max]