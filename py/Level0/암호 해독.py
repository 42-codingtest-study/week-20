#
# [level 0] 암호 해독
# https://school.programmers.co.kr/learn/courses/30/lessons/120892

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(cipher, code):
    word = list(cipher)
    word.insert(0, '0')
    result = ""

    for i in range(code, len(word)):
        if i % code == 0:
            result += word[i]

    return result