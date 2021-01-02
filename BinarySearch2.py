
N,M=map(int,input().split())
long=list(map(int,input().split()))
'''
def test(arr,target,start,end):
    if start>end:
        return None
    mid=(start+end)//2
    est=[mid-1,mid,mid+1]
    for i in range(3):
        if getsum(est[i],arr)==target:
            return est[i]
        if i!=2 and getsum(est[i+1],arr)<target<getsum(est[i],arr):
            return est[i]
    if target<getsum(est[i],arr):
        test(arr,target,0,mid)
    else:
        test(arr,target,mid,end)
 
def getsum(v,arr):
   result=0
   for element in arr:
       if element>v:
           result+=(element-v)
   return result

print(test(lens,M,0,N))
'''
start=0
end=max(long)
while start<end:
    mid=(start+end)//2
    result=0
    for i in long:
        if mid<i:
            result+=i-mid
    if result==M:
        break
    elif result>M:
        start=mid
    else:
        end=mid
print(mid)