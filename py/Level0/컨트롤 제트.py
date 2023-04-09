#
# [level 0] 컨트롤 제트
# https://school.programmers.co.kr/learn/courses/30/lessons/120853

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(s):
    sum = 0
    num = list(s.split(' '))

    for i in range(len(num)):
        if num[i] == 'Z':
            sum -= int(num[i - 1])
        else:
            sum += int(num[i])

    return sum