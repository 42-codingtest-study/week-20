#
# [level 0] 중복된 문자 제거
# https://school.programmers.co.kr/learn/courses/30/lessons/120888

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(my_string):
    return ''.join(dict.fromkeys(my_string))