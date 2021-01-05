N,M=map(int,input().split())
coins=[]
for i in range(N):
    coins.append(int(input()))
memo=[99999]*(M+1)
for i in range(M+1):
    if i in coins:
        memo[i]=1
    for coin in coins:
        try:
            memo[i]=min(memo[i-coin]+1,memo[i])
        except:
            pass

if memo[i]==99999:
    print(-1)
else:
    print(memo[i])