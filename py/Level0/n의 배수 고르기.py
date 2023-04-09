#
# [level 0] n의 배수 고르기
# https://school.programmers.co.kr/learn/courses/30/lessons/120905

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(n, numlist):
    return [i for i in numlist if i % n == 0]