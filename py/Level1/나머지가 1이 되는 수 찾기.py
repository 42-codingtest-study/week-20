#
# [level 1] 나머지가 1이 되는 수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/87389

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(n):
    for x in range(2, 1000000):
        if n % x == 1:
            return x