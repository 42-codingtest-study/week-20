#
# [level 0] 평행
# https://school.programmers.co.kr/learn/courses/30/lessons/120875

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(dots):
    answer = 0
    # 1번점 - 2번점
    a = (dots[0][1] - dots[1][1]) / (dots[0][0] - dots[1][0])
    b = (dots[2][1] - dots[3][1]) / (dots[2][0] - dots[3][0])

    # 1번점 - 3번점
    c = (dots[0][1] - dots[2][1]) / (dots[0][0] - dots[2][0])
    d = (dots[1][1] - dots[3][1]) / (dots[1][0] - dots[3][0])

    # 1번점 - 4번점
    e = (dots[0][1] - dots[3][1]) / (dots[0][0] - dots[3][0])
    f = (dots[1][1] - dots[2][1]) / (dots[1][0] - dots[2][0])

    if a == b:
        return 1
    elif c == d:
        return 1
    elif e == f:
        return 1
    else:
        return 0