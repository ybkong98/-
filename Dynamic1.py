x=int(input())
d=[0]*(x+1)
for n in range(x+1):
    if n<=1:
        pass
    else:
        d[n]=d[n-1]+1
        if n%2==0:
            d[n]=min(d[n],d[n//2]+1)
        if n%3==0:
            d[n]=min(d[n],d[n//3] +1)
        if n%5==0:
            d[n]=min(d[n],d[n//5] +1)
print(d[-1])    
        