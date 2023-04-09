#
# [level 1] 자릿수 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12912

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(a, b):
    return sum(range(min(a, b), max(a, b) + 1))