n=int(input())
l=list(map(int,input().split()))
d=[]
c=[]
for i in l:
    if i==l.count(i):
        d.append(i)
for j in d:
    if j not in c:
        c.append(j)
print(len(c))
            
    