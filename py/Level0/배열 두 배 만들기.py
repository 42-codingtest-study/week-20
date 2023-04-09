#
# [level 0] 배열 두 배 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/120841

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(numbers):
    answer = []

    for i in numbers:
        answer.append(i * 2)
    return answer