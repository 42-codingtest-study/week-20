# 질문
#
# [level 0] 겹치는 선분의 길이
# https://school.programmers.co.kr/learn/courses/30/lessons/120876

# 결과
# 정확성: 80.0
# 합계: 80.0 / 100.0

def solution(lines):
    line = []
    for i in lines:
        line.append([j for j in range(i[0], i[1] + 1)])

    a, b, c = line[0], line[1], line[2]
    result = []
    answer = 0

    for i in a:
        for j in b:
            if i == j: result.append(i)

    for j in b:
        for k in c:
            if j == k:
                if j not in result:
                    result.append(j)

    for k in c:
        for i in a:
            if k == i:
                if k not in result:
                    result.append(k)

    result.sort()

    if len(result) < 2: return 0

    for i in range(0, len(result) - 1):
        if (result[i] + 1) == result[i + 1]: answer += 1

    return answer