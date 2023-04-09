min_value = 2000
min_value_drink = 2000

for i in range(3):
    a = int(input())
    min_value = min(a, min_value)
for i in range(2):
    a = int(input())
    min_value_drink = min(a, min_value_drink)
    
print(min_value+min_value_drink - 50)
    
    