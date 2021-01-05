from heapq import *
N,M,C=map(int,input().split())
path=[[] for _ in range(N+1)]
for _ in range(M):
    X,Y,Z=map(int,input().split())
    path[X].append((Z,Y))
distance=[654321]*(N+1)
q=[]
heapify(q)
heappush(q,(0,C))
distance[C]=0
while q:
    dist,now=heappop(q)
    if distance[now]<dist:
        continue
    for node in path[now]:
        cost=dist+node[1]
        if cost<distance[node[0]]:
            distance[node[0]]=cost
            heappush(q,(cost,node[0]))

for city in distance:
    if city==654321:
        distance.remove(city)
print(len(distance),max(distance))