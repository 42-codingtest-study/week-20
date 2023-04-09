#
# [level 1] 자릿수 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12910

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(arr, divisor):
    num = [i for i in arr if i % divisor == 0]

    if len(num) == 0:
        return [-1]
    else:
        num.sort()
        return num