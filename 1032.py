N = int(input())

answer = list(input())

for _ in range(0, N - 1) : 
	file_name = list(input())
	for c in range(0, len(file_name)) :
		if answer[c] == file_name[c] :
			continue
		else :
			answer[c] = '?'

print(''.join(answer)) 
