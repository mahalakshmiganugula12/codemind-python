n=int(input())
l=list(map(str,input().split()))
C=0
for i in l:
    if len(i)%2==0:
        C+=1
print(C)