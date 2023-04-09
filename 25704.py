N = int(input())
price = int(input())
sale = [0]

if N >= 5 :
    sale.append(500)	
if N >= 10 :
    sale.append(price // 10)	
if N >= 15 :
    sale.append(2000)	
if N >= 20 :
    sale.append(price // 4)	

res = price - max(sale)
if res < 0 :
    res = 0	
print(res)