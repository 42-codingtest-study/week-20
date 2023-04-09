#
# [level 1] 문자열 다루기 기본
# https://school.programmers.co.kr/learn/courses/30/lessons/12918

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(s):
    if len(s) == 4 or len(s) == 6:
        return s.isdigit()
    else: return False