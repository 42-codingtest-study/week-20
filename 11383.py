n, m = map(int, input().split())

arr1 = [input() for _ in range(n)]
arr2 = [input() for _ in range(n)]

pre_arr = ['' for _ in range(n)]

for i in range(0, n) :
	for j in range(0, m*2, 2):
		if arr2[i][j] != arr2[i][j + 1]:
			print("Not Eyfa")
			exit()
		pre_arr[i] += arr2[i][j]

for i in range(0, n) :
	if arr1[i] != pre_arr[i] :
		print("Not Eyfa")
		exit()

print("Eyfa")