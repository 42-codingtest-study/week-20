#
# [level 0] 개미 군단
# https://school.programmers.co.kr/learn/courses/30/lessons/120837

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(hp):
    a = hp // 5  # 장군개미
    b = hp % 5 // 3  # 병정개미
    c = hp % 5 % 3  # 일개미

    return a + b + c