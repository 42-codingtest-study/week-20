#
# [level 0] 대문자와 소문자
# https://school.programmers.co.kr/learn/courses/30/lessons/120893

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(my_string):
    answer = ''

    for i in my_string:
        if i.islower():
            answer += i.upper()
        else:
            answer += i.lower()

    return answer