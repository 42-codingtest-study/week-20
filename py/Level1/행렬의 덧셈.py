#
# [level 1] 행렬의 덧셈
# https://school.programmers.co.kr/learn/courses/30/lessons/12950

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]

    return arr1