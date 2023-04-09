#
# [level 0] 최댓값 만들기 (2)
# https://school.programmers.co.kr/learn/courses/30/lessons/120862

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(numbers):
    numbers.sort()

    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])