#
# [level 0] 저주의 숫자 3
# https://school.programmers.co.kr/learn/courses/30/lessons/120871

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(n):
    x = 0
    for i in range(n):
        x += 1

        while x % 3 == 0 or '3' in str(x):
            x += 1
    return x