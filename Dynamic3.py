N=int(input())
memo=[0]*(N+1)
for i in range(N+1):
    if i==1:
        memo[i]=1
    elif i==2:
        memo[i]=3
    else:
        memo[i]=memo[i-1]+memo[i-2]*2
print(memo)