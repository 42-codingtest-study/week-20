#
# [level 0] 최빈값 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120812

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(array):
    if len(array) == 1:
        return array[0]

    dict = {}

    for i in array:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    k = list(dict.keys())
    v = list(dict.values())

    # 동일한 값만 있을 경우 [2, 2, 2, 2]
    if len(k) == 1:
        return k[0]

    re_v = sorted(v, reverse=True)

    if re_v[0] == re_v[1]:
        return -1
    else:
        return k[v.index(max(v))]