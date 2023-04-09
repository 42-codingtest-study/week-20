#
# [level 0] 영어가 싫어요
# https://school.programmers.co.kr/learn/courses/30/lessons/120894

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(numbers):
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for index, num in enumerate(nums):
        numbers = numbers.replace(num, str(index))

    return int(numbers)