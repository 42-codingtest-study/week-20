#
# [level 0] 이진수 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120885

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(bin1, bin2):
    a = int(bin1, 2)
    b = int(bin2, 2)

    return bin(a + b)[2:]