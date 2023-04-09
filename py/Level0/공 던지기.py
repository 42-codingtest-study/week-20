#
# [level 0] 공 던지기
# https://school.programmers.co.kr/learn/courses/30/lessons/120843

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(numbers, k):
    return numbers[2 * (k - 1) % len(numbers)]