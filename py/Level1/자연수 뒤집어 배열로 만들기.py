#
# [level 1] 자연수 뒤집어 배열로 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12932

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(n):
    answer = list(map(int, str(n)))
    return answer[::-1]