n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())

sum=0
for i in l:
    if a>i or b<i:
    
        sum=sum+i
print(sum)