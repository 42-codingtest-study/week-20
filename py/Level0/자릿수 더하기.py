#
# [level 0] 자릿수 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120906

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(n):
    num = list(map(int, str(n)))

    return sum(i for i in num)