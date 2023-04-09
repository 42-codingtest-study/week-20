#
# [level 0] 문자열 밀기
# https://school.programmers.co.kr/learn/courses/30/lessons/120921

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(A, B):
    chka = list(A)
    chkb = list(B)

    if chka == chkb:
        return 0
    else:
        for i in range(len(A)):
            chka.insert(0, chka.pop())
            if chka == chkb: return i + 1

        return -1