#
# [level 0] 삼각형의 완성 조건 (2)
# https://school.programmers.co.kr/learn/courses/30/lessons/120868

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(sides):
    sides.sort(reverse=True)

    answer = []

    # 가장 긴 변이 주어진 경우
    for i in range(1, sides[0]):
        if sides[0] < sides[1] + i:
            if i not in answer:
                answer.append(i)

    # 가장 긴 변을 찾아야 하는 경우
    for i in range(sides[0], 10000):
        if i < sum(sides):
            if i not in answer:
                answer.append(i)

    return len(answer)