from collections import deque
N,M=map(int,input().split())
maze=[list(map(int,input())) for _ in range (N)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def run(x,y):
    q=deque()
    q.append((x,y))
    while q:
        x,y=q.popleft()
        for move in zip(dx,dy):
            newx=x+move[0]
            newy=y+move[1]
            if newx not in range(N) or newy not in range(M):
                continue
            if maze[newx][newy]==0:
                continue
            else:
                if maze[newx][newy]==1:
                    maze[newx][newy]=maze[x][y]+1
                    q.append((newx,newy))
    return maze[-1][-1]
print(run(0,0))