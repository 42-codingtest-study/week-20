#
# [level 0] 외계어 사전
# https://school.programmers.co.kr/learn/courses/30/lessons/120869

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

from itertools import permutations

def solution(spell, dic):
    word = [''.join(i) for i in permutations(spell, len(spell))]

    for i in dic:
        for j in word:
            if i == j:
                return 1
    return 2