#
# [level 1] 자릿수 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12931

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(n):
    answer = 0
    num = list(map(int, str(n)))

    for i in num:
        answer += i

    return answer