#
# [level 0] OX퀴즈
# https://school.programmers.co.kr/learn/courses/30/lessons/120907

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(quiz):
    result = []
    for q in quiz:
        chk = list(q.split(' '))

        if chk[1] == '+':
            x = int(chk[0]) + int(chk[2])
        else:
            x = int(chk[0]) - int(chk[2])

        result.append("O" if x == int(chk[4]) else "X")

    return result