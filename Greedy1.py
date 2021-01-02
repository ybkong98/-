money=int(input())
coin=[500,100,50,10]
n=[]
for penny in coin:
    n.append(money//penny)
    money%=penny

print(n)