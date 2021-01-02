N,M=map(int,input().split())
cards=[list(map(int,input().split())) for _ in range(N)]
mins=[]
for i in range(N):
    mins.append(min(cards[i]))
print(max(mins))