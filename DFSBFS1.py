N,M=map(int,input().split())
block=[list(map(int,input())) for _ in range (N)]
def judge(x,y):
    if x in range(N) and y in range(M):
        if block[x][y]==1:
            return False
        if block[x][y]==0:
            block[x][y]=1
            judge(x-1,y)
            judge(x+1,y)
            judge(x,y-1)
            judge(x,y+1)
            return True
    else:
        return False

count=0
for i in range(N):
    for j in range(M):
        if judge(i,j):
            count+=1
print(count)

