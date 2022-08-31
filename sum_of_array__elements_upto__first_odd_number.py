n=int(input())
l=list(map(int,input().split()))
d=[]
for i in l:
    if i%2!=0:
        break
    d.append(i)
print(sum(d))
    
    
