#
# [level 0] 짝수는 싫어요
# https://school.programmers.co.kr/learn/courses/30/lessons/120813

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(n):
    answer = []

    for i in range(1, n + 1):
        if i % 2 != 0:
            answer.append(i)

    return answer

