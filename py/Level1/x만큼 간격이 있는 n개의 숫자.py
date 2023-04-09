#
# [level 1] x만큼 간격이 있는 n개의 숫자
# https://school.programmers.co.kr/learn/courses/30/lessons/12954

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(x, n):
    answer = []
    y = x
    for i in range(n):
        answer.append(y)
        y += x

    return answer