N=int(input())
nlist=list(map(int,input().split()))
M=int(input())
mlist=list(map(int,input().split()))
for target in mlist:
    if target in nlist:
        print('yes',end=' ')
    else:
        print('no',end=' ')