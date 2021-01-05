n=int(input())
blocks=list(map(int,input().split()))
memo=[0]*n
for i in range(n):
    if i<2:
        memo[i]=max(blocks[:i+1])
    else:
        memo[i]=max(memo[i-2]+blocks[i],memo[i-1])

print(memo[-1])