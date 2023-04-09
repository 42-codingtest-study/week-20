#
# [level 0] 다항식 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120863

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(polynomial):
    num = polynomial.split(' + ')
    x, n = 0, 0

    for i in num:
        if 'x' in i:
            if len(i) > 1:
                x += int(i[:-1])
            else:
                x += 1
        else:
            n += int(i)

    if x == 0:
        return str(n)
    elif x == 1:
        if n == 0:
            return 'x'
        else:
            return "x + {0}".format(n)
    elif x > 1:
        if n == 0:
            return "{0}x".format(x)
        else:
            return "{0}x + {1}".format(x, n)