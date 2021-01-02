array=[]
N=int(input())
for _ in range(N):
    array.append(int(input()))
array.sort(reverse=True)
for i in range(N):
    print(array[i],end=' ')