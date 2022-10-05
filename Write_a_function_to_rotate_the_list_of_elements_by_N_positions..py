n=int(input())
l=list(map(int,input().split()))
m=int(input())
if m>n:
    m=m%n
z=l[-m:]+l[:-m]
print(*z)