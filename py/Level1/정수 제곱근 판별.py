#
# [level 1] 정수 제곱근 판별
# https://school.programmers.co.kr/learn/courses/30/lessons/12934

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

import math

def solution(n):
    return (math.sqrt(n) + 1) ** 2 if math.sqrt(n) == int(math.sqrt(n)) else -1