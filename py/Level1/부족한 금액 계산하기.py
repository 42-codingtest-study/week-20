#
# [level 1] 부족한 금액 계산하기
# https://school.programmers.co.kr/learn/courses/30/lessons/82612

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(price, money, count):
    total = 0
    for i in range(count):
        total += price * (i + 1)

    return total - money if money < total else 0
