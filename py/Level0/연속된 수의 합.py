#
# [level 0] 연속된 수의 합
# https://school.programmers.co.kr/learn/courses/30/lessons/120923

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(num, total):
    middle_idx = num // 2  # 기준 수 양쪽으로 더하거나 빼야할 숫자 개수
    middle_num = total // num  # 가운데 or 가운데 왼쪽 들어가는 숫자

    start_num = middle_idx * - 1 if num % 2 == 1 else middle_idx * -1 + 1
    end_num = middle_idx + 1

    answer = [num + middle_num for num in range(start_num, end_num)]

    return answer