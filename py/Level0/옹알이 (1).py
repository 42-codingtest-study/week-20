#
# [level 0] 옹알이 (1)
# https://school.programmers.co.kr/learn/courses/30/lessons/120956

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

from itertools import permutations


def solution(babbling):
    say = ["aya", "ye", "woo", "ma"]
    word = []
    answer = 0

    for i in range(1, len(say) + 1):
        for j in permutations(say, i):
            word.append(''.join(j))

    for i in babbling:
        if i in word:
            answer += 1

    return answer