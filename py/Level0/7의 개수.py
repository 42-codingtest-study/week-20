#
# [level 0] 7의 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/120912

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(array):
    cnt = 0
    for i in array:
        if '7' in str(i):
            cnt += str(i).count('7')
    return cnt