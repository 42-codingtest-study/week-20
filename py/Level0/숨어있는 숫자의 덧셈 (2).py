#
# [level 0] 숨어있는 숫자의 덧셈 (2)
# https://school.programmers.co.kr/learn/courses/30/lessons/120864

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

# my_string이 숫자로 끝나는 경우

def solution(my_string):
    sum = 0
    num = ""

    for i in range(len(my_string)):
        if my_string[i].isdigit():
            num += my_string[i]
        else:
            if len(num) != 0:
                sum += int(num)
                num = ""
    if len(num) != 0:
        sum += int(num)

    return sum