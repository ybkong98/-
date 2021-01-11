from collections import deque
N=int(input())
time=[99999]
pre=[[]]
result=[0]
done=[]
#의미없는 값을 넣어줘서 인덱스가 1부터 시작하도록 만들어줌. result는 반복문에 쓰기 위해 첫값을 0으로 만듦 
for _ in range(N):
    inp=list(map(int,input().split()))
    time.append(inp[0])
    pre.append(inp[:-1])
q=deque()
q.append(1)
while q:
    now=q.popleft()
    result.append(result[now-1]+time[now])
    done.append(now)
    for lectures in pre:
        if lectures in done:
            for lecture in lectures:
                q.append(lecture)

print(result[1:])
#Error...