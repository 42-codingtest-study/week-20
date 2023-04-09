#
# [level 1] 최대공약수와 최소공배수
# https://school.programmers.co.kr/learn/courses/30/lessons/12940

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(n, m):
    answer = []

    for i in range(1, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            x = i
    answer.append(x)

    for i in range(max(n, m), 1000000):
        if i % n == 0 and i % m == 0:
            answer.append(i)
            break
    return answer