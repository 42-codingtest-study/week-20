#
# [level 0] 모음 제거
# https://school.programmers.co.kr/learn/courses/30/lessons/120849

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(my_string):
    vowel = ['a', 'e', 'i', 'o', 'u']

    for i in vowel:
        my_string = my_string.replace(i, '')

    return my_string