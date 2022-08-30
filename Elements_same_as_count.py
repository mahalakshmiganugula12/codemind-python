n=int(input())
l=list(map(int,input().split()))
d=[]
c=[]
s=0
for i in l:
    if l.count(i)==i:
        s=1
        if i in d:
            
            continue
        
        
        d.append(i)
if s==0:
    print("-1")
else:
    print(*d)
        
 
        