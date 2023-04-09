#
# [level 1] 서울에서 김서방 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/12919

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(seoul):
    for i in seoul:
        if i == "Kim":
            return ("김서방은 %s에 있다" %seoul.index(i))