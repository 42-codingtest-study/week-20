#
# [level 0] 주사위의 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/120845

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(box, n):
    return (box[0] // n) * (box[1] // n) * (box[2] // n)