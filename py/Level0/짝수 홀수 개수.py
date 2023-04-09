#
# [level 0] 짝수 홀수 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/120824

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(num_list):
    odd = 0
    even = 0

    for i in num_list:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    return [even, odd]