a=120
# 1 2 3 4 5 6 8 10 12 15 ... for迴圈
ans = 0
for i in  range(1, a+1):
  if a%1==0:
    print( i, end=' ')
    ans += 1
print('有幾個整除? ', ans)
