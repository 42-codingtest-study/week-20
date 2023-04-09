#
# [level 0] 한 번만 등장한 문자
# https://school.programmers.co.kr/learn/courses/30/lessons/120896

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(s):
    dict = {}

    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    key = list(dict.keys())
    va = list(dict.values())
    answer = []

    for i in range(0, len(va)):
        if va[i] == 1:
            answer.append(key[i])

    return ''.join(sorted(answer))