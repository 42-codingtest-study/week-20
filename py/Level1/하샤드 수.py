#
# [level 1] 자릿수 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12947

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(x):
    n = [int(i) for i in str(x)]

    return True if x % sum(n) == 0 else False