n = int(input())
s = 0
for i in range(n):
    if i * (i + 1) == n:
        s = 1
        break
if s==1:
    print("YES")
else:
    print("NO")