n = input()
n_len = len(n)
flag = 0

for i in range(n_len - 1):
    n_left = 1
    n_right = 1
    for j in range(i + 1):
        n_left *= int(n[j])
    for k in range(i + 1, n_len):
        n_right *= int(n[k])
    if n_left == n_right:
        print("YES")
        flag = 1
        break

if flag == 0:
    print("NO")