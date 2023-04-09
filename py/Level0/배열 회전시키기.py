#
# [level 0] 배열 회전시키기
# https://school.programmers.co.kr/learn/courses/30/lessons/120844

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(numbers, direction):
    if direction == 'right':
        numbers.insert(0, numbers[-1])
        numbers.pop()
        return numbers
    else:
        numbers.append(numbers[0])
        numbers.remove(numbers[0])
        return numbers