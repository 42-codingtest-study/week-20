#
# [level 0] 배열 원소의 길이
# https://school.programmers.co.kr/learn/courses/30/lessons/120854

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(strlist):
    answer = []

    for i in strlist:
        answer.append(len(i))

    return answer