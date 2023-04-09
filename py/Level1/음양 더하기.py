#
# [level 1] 음양 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/76501

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(absolutes, signs):
    answer = 0

    for i in range(len(signs)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]

    return answer