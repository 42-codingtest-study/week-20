#
# [level 0] 숨어있는 숫자의 덧셈 (1)
# https://school.programmers.co.kr/learn/courses/30/lessons/120851

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit())