n=int(input())
l=list(map(int,input().split()))
k=int(input())
d=[]
for i in range(k):
    d.append(l[i])
    c=sum(d)
print(c)
    
