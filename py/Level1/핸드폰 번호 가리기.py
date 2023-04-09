#
# [level 1] 자릿수 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12948

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(phone_number):
    phone = "*" * len(phone_number[:-4]) + phone_number[-4:]
    return phone