#
# [level 0] 369게임
# https://school.programmers.co.kr/learn/courses/30/lessons/120891

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(order):
    return str(order).count('3') + str(order).count('6') + str(order).count('9')