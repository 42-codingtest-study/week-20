#
# [level 1] 가운데 글자 가져오기
# https://school.programmers.co.kr/learn/courses/30/lessons/12903

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(s):
    if len(s) % 2 == 0:
        return s[len(s) // 2 - 1:len(s) // 2 + 1]
    else:
        return s[len(s) // 2]