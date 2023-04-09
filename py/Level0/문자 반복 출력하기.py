#
# [level 0] 문자 반복 출력하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120825

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer += i * n

    return answer