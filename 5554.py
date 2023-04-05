hs = int(input())
spc = int(input())
pca = int(input())
ah = int(input())
res = 0
x, y = 0, 0
res = hs + spc + pca + ah
x = res // 60
y = res % 60

print(x)
print(y)