N,M=map(int,input().split())
connections=[[654321]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a,b= map(int,input().split())
    connections[a][b]=1
    connections[b][a]=1
X,K=map(int,input().split())

for k in range(N+1):
    for i in range(N+1):
        for j in range(N+1):
            connections[i][j]=min(connections[i][j],connections[i][k]+connections[k][j])
            connections[j][i]=connections[i][j]
cost=connections[1][K]+connections[K][X]
if cost==654321*2:
    print(-1)
else:
    print(cost)