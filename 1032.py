num = int(input())

word = list(input())                  
word_len = len(word)        

for i in range(0, num - 1):         
    b = list(input())
    for j in range(0, word_len):       
        if word[j] != b[j]:            
            word[j] = '?'

print("".join(word))