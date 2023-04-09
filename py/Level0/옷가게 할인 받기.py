#
# [level 0] 옷가게 할인 받기
# https://school.programmers.co.kr/learn/courses/30/lessons/120818

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(price):
    if price >= 500000:
        return int(price * 0.8)
    elif price >= 300000:
        return int(price * 0.9)
    elif price >= 100000:
        return int(price * 0.95)
    else:
        return price