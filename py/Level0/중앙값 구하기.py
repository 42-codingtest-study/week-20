#
# [level 0] 중앙값 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120811

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(array):
    array.sort()

    return array[len(array) // 2]