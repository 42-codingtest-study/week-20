#
# [level 0] 직사각형 넓이 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120860

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(dots):
    if dots[0][0] == dots[1][0]:
        return abs(dots[0][1] - dots[1][1]) * abs(dots[0][0] - dots[2][0])
    elif dots[0][0] == dots[2][0]:
        return abs(dots[0][1] - dots[2][1]) * abs(dots[0][0] - dots[1][0])
    elif dots[0][0] == dots[3][0]:
        return abs(dots[0][1] - dots[3][1]) * abs(dots[0][0] - dots[1][0])