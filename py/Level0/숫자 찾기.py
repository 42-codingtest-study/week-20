#
# [level 0] 숫자 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/120904

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(num, k):
    if str(k) in str(num):
        return str(num).find(str(k)) + 1
    else:
        return -1