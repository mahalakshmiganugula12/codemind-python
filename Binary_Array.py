n=int(input())
l=list(map(int,input().split()))
d=[]
f=len(l)
for i in l:
    if i==0 or i==1:
        d.append(i)
if f==len(d):
    print("True")
else:
    print("False")