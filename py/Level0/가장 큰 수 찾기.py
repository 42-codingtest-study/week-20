#
# [level 0] 가장 큰 수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/120899

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(array):
    return [max(array), array.index(max(array))]