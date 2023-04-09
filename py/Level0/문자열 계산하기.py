#
# [level 0] 문자열 계산하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120902

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(my_string):
    sen = list(my_string.split(' '))
    answer = int(sen[0])

    for i in range(len(sen)):
        if sen[i] == '+':
            answer += int(sen[i + 1])
        elif sen[i] == '-':
            answer -= int(sen[i + 1])

    return answer