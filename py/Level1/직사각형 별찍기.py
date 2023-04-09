#
# [level 1] 직사각형 별찍기
# https://school.programmers.co.kr/learn/courses/30/lessons/12969

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

a, b = map(int, input().strip().split(' '))

for i in range(b):
    print("*" * a)