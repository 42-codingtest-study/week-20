#
# [level 0] 진료순서 정하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120835

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(emergency):
    sort_emergency = sorted(emergency, reverse=True)
    answer = []

    for i in emergency:
        for j in sort_emergency:
            if i == j:
                answer.append(sort_emergency.index(j) + 1)

    return answer