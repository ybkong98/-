N,M=map(int,input().split())
X,Y,D=map(int,input().split())
world=[list(map(int,input().split())) for _ in range(N)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def move(x,y,turn,count):
    world[x][y]=999999
    #임의로 값을 줘서 방문 처리
    for i in range(4):
       a=(turn-(i+1))%4
       newx=x+dx[a]
       newy=y+dy[a]
       if newx not in range(M) or newy not in range(N):
           continue
       if world[newx][newy]==0:
           count=count+1
           move(newx,newy,a,count)
    prex,prey=x+dx[turn-2],y+dy[turn-2]
    if world[prex][prey]==1:
        return count+1
    else:
        move(prex,prey,turn,count)

print(move(X,Y,D,1))