#
# [level 0] 배열의 유사도
# https://school.programmers.co.kr/learn/courses/30/lessons/120903

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(s1, s2):
    answer = [i for i in s1 if i in s2]

    return len(answer)