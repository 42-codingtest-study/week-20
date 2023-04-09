#
# [level 1] 수박수박수박수박수박수?
# https://school.programmers.co.kr/learn/courses/30/lessons/12922

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(n):
    return "수박" * (n // 2) + "수" * (n % 2)