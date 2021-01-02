pos=input()
loc=[int(ord(pos[0]))-int(ord('a'))+1,int(pos[1])]
#Type error 방지 위해 새로 만들어준다.
moves=[(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(-2,1),(2,-1),(-2,-1)]
count=0
for move in moves:
    if move[0]+loc[0] in range(1,9) and move[1]+loc[1] in range(1,9):
        count+=1
print(count)