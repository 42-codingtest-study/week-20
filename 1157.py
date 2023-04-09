#런타임 에러
word = input().upper()
word_list = list(set(word))
lst = []

for i in word_list:
    cnt = word.cnt(i)
    lst.append(cnt)

if lst.cnt(max(lst))>= 2:
    print("?")
else:
    print(word_list[lst.index(max(lst))])