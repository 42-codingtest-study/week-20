#
# [level 0] 2차원으로 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/120842

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(num_list, n):
    answer = []

    for i in range(len(num_list) // n):
        answer.append(num_list[i * n: (i + 1) * n])

    return answer

