#
# [level 1] 약수의 합
# https://school.programmers.co.kr/learn/courses/30/lessons/12928

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(n):
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sum += i

    return sum