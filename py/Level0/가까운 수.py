#
# [level 0] 가까운 수
# https://school.programmers.co.kr/learn/courses/30/lessons/120890

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(array, n):
    array.sort()
    cnt = [abs(i - n) for i in array]
    return array[cnt.index(min(cnt))]