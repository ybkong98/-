'''
N=int(input())
count=0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            string=str(i)+str(j)+str(k)
            if '3' in string:
                count+=1
print(count)
'''

N=int(input())
count=0
for i in range(N+1):
    if '3' in str(i):
        count+=3600
    else:
        for j in range(60):
            if '3' in str(j):
                count+=60
            else:
                for k in range(60):
                    if '3' in str(k):
                        count+=1
print(count)