#
# [level 1] 콜라츠 추측
# https://school.programmers.co.kr/learn/courses/30/lessons/12943

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(num):
    if num == 1:
        return 0

    for i in range(500):
        num = num / 2 if num % 2 == 0 else num * 3 + 1

        if num == 1:
            return i + 1
    return -1