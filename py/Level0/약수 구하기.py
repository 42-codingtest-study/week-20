#
# [level 0] 약수 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120897

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(n):
    return [i for i in range(1, n + 1) if n % i == 0]