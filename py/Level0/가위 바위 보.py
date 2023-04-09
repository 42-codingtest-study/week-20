#
# [level 0] 가위 바위 보
# https://school.programmers.co.kr/learn/courses/30/lessons/120839

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(rsp):
    dict = {
        "0": "5",
        "2": "0",
        "5": "2"
    }
    order = list(rsp)
    answer = ""

    for i in order:
        answer += dict[i]

    return answer