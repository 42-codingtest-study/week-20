#
# [level 1] 자릿수 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12935

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        arr.remove(min(arr))

    return arr