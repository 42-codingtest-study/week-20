#
# [level 0] 합성수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/120846

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(n):
    cnt = 0

    for i in range(4, n + 1):
        chk = 0
        for j in range(1, i + 1):
            if i % j == 0:
                chk += 1
        if chk >= 3:
            cnt += 1
    return cnt