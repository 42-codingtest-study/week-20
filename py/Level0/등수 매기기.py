#
# [level 0] 등수 매기기
# https://school.programmers.co.kr/learn/courses/30/lessons/120882

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(score):
    chk = []
    answer = []
    for i in score:
        chk.append((i[0] + i[1]) / 2)

    chk_sort = sorted(chk, reverse=True)

    for i in range(len(chk_sort)):
        answer.append(chk_sort.index(chk[i]) + 1)
    return answer