#
# [level 0] 잘라서 배열로 저장하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120913

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(my_str, n):
    answer = []
    while len(my_str) >= n:
        answer.append(my_str[:n])
        my_str = my_str[n:]

    if len(my_str) != 0:
        answer.append(my_str)

    return answer