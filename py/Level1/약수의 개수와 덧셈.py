#
# [level 1] 약수의 개수와 덧셈
# https://school.programmers.co.kr/learn/courses/30/lessons/77884

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        cnt = [j for j in range(1, i + 1) if i % j == 0]

        if len(cnt) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer