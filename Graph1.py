N,M=map(int,input().split())
parent=list(range(N+1))
results=[]
def matching(parent,x):
    if parent[x]!=x:
        parent[x]=matching(parent,parent[x])
    return parent[x]

    
def union(a,b):
    global parent
    a=matching(parent,a)
    b=matching(parent,b)
    if check(a,b)=='NO':
        if a<b:
            parent[b]=a
        else:
            parent[a]=b

def check(a,b):
    global parent
    if parent[a]==parent[b]:
        return 'YES'
    else:
        return 'NO'


for _ in range(M):
    op,a,b=map(int,input().split())
    if op==0:
        union(a,b)
    elif op==1:
        results.append(check(a,b))

for result in results:
    print(result)