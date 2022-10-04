n=int(input())
l=list(map(int,input().split()))
b=[]
for i in l:
    if i%2==0:
        b.append(i)
for j in l:
    if j%2!=0:
        b.append(j)
print(*b)