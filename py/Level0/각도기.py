#
# [level 0] 각도기
# https://school.programmers.co.kr/learn/courses/30/lessons/120829

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(angle):
    if 0 < angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif 90 < angle < 180:
        return 3
    elif angle == 180:
        return 4