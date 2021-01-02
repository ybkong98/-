n,m,k=map(int,input().split())
data=list(map(int,input().split()))
result=0
number1=data.pop(data.index(max(data)))
number2=data.pop(data.index(max(data)))
while m>0:
    for _ in range(k):
        result+=number1
        m-=1
    if m==0:
        break
    result+=number2
    m-=1

print(result)
