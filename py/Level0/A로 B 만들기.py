#
# [level 0] A로 B 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/120886

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(before, after):
    if ''.join(sorted(before)) == ''.join(sorted(after)):
        return 1
    else:
        return 0