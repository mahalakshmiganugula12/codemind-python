n=int(input())
l=list(map(int,input().split()))
c=[]
d=[]
for i in l:
    c.append(len(str(i)))
for j in l:
    if len(str(j))==max(c):
        d.append(j)
print(*d)
    