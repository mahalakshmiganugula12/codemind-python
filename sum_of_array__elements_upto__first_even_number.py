n=int(input())
l=list(map(int,input().split()))
d=[]
c=0
for i in l:
    if i%2==0:
        break
    d.append(i)
    c=sum(d)
print(c)
        