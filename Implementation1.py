N=int(input())
plan=list(input().split())
pos=[1,1]
for move in plan:
    if move=='R':
        if pos[1]==N:
            pass
        else:
            pos[1]+=1    
    elif move=='L':
        if pos[1]==1:
            pass
        else:
            pos[1]-=1  
    elif move=='U':
        if pos[0]==1:
            pass
        else:
            pos[0]-=1  
    elif move=='D':
        if pos[0]==N:
            pass
        else:
            pos[0]+=1
            
print(pos[0], pos[1])