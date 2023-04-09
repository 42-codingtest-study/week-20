#
# [level 0] 로그인 성공?
# https://school.programmers.co.kr/learn/courses/30/lessons/120883

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(id_pw, db):
    for i in db:
        if i[0] == id_pw[0]:
            if i[1] == id_pw[1]:
                return "login"
            else:
                return "wrong pw"

    return "fail"