#
# [level 0] 캐릭터의 좌표
# https://school.programmers.co.kr/learn/courses/30/lessons/120861

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(keyinput, board):
    garo = board[0] // 2
    sero = board[1] // 2

    answer = [0, 0]

    for i in keyinput:
        if i == "left":
            answer[0] -= 1
            if answer[0] < -garo:
                answer[0] = -garo
        elif i == "right":
            answer[0] += 1
            if answer[0] > garo:
                answer[0] = garo
        elif i == "up":
            answer[1] += 1
            if answer[1] > sero:
                answer[1] = sero
        elif i == "down":
            answer[1] -= 1
            if answer[1] < -sero:
                answer[1] = -sero

    return answer