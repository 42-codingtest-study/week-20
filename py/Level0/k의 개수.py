#
# [level 0] k의 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/120887

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(i, j, k):
    num = []

    for x in range(i, j + 1):
        num.append(str(x))

    return sum(x.count(str(k)) for x in num)
