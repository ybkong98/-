N,K=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
arr1.sort()
arr2.sort(reverse=True)
#arr1은 오름차순, arr2는 내림차순으로 정렬
for i in range(K):
    if arr1[i]<arr2[i]:
        arr1[i],arr2[i]=arr2[i],arr1[i]

print(sum(arr1))