N,M=map(int,input().split())
parent=list(range(N+1))
edges=[]
result=0
for _ in range(M):
    a,b,c=map(int,input().split())
    edges.append((c,(a,b)))
edges.sort(key=lambda data: data[0])
#입력+edge를 cost 기준으로 정렬
def matching(parent,x):
    if parent[x]!=x:
        parent[x]=matching(parent,parent[x])
    return parent[x]

    
def union(a,b):
    global parent
    a=matching(parent,a)
    b=matching(parent,b)
    if not check(a,b):
        if a<b:
            parent[b]=a
        else:
            parent[a]=b

def check(a,b):
    global parent
    if parent[a]==parent[b]:
        return True
    else:
        return False
#Graph1.py 에서 사용했던 함수 그대로 인용

for edge in edges:
    cost=edge[0]
    a,b=edge[1]
    if not check(a,b):
        union(a,b)
        result+=cost

print(result)
#어떻게 2개로....?