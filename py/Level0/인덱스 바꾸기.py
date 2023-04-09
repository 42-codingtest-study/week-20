#
# [level 0] 인덱스 바꾸기
# https://school.programmers.co.kr/learn/courses/30/lessons/120895

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(my_string, num1, num2):
    str = list(my_string)
    a = str[num1]
    b = str[num2]

    str[num1] = b
    str[num2] = a

    return ''.join(str)