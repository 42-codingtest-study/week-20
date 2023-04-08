a = list(input())
for c in range (0, len(a)) :
	a[c] = int(a[c])

for i in range(0, len(a) - 1) :
	tmp1, tmp2 = 1, 1
	for j in range (0, i + 1):
		tmp1 *= a[j]
	for k in range (i + 1, len(a)):
		tmp2 *= a[k]
	if tmp1 == tmp2 :
		print("YES")
		exit()

print("NO")