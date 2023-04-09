#
# [level 0] 제곱수 판별하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120909

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

import math

def solution(n):
    if math.sqrt(n) == int(math.sqrt(n)):
        return 1
    else:
        return 2