#
# [level 0] 순서쌍의 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/120836

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(n):
    cnt = 0

    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1

    return cnt