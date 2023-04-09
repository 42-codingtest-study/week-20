# 질문
#
# [level 0] 안전지대
# https://school.programmers.co.kr/learn/courses/30/lessons/120892

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(board):
    n = len(board)
    chk = []
    # 1 있는 곳 확인
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                chk.append((i, j))

    # 지뢰가 설치된 곳 주변에 폭탄 설치
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    for x, y in chk:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                board[nx][ny] = 1

    # 폭탄 없는 곳만 세기
    answer = 0
    for cnt in board:
        answer += cnt.count(0)

    return answer