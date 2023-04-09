#
# [level 1] 자릿수 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/86051

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(numbers):
    s = sum(i for i in range(10))
    n = sum(i for i in numbers)

    return s - n