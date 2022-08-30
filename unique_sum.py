n=int(input())
l=list(map(int,input().split()))
d=[]
for i in l:
    if i in d:
        continue
    
    d.append(i)
print(sum(d))