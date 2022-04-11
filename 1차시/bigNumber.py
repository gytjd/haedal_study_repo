#큰 수의 법칙-Greedy Algorithm

n,m,k=map(int,input().split())
data=list(map(int,input().split()))

          
data.sort(reverse=True)
f=data[0]
s=data[1]
result=0

while m!=0:
    for i in range(k):
        result+=f
        m-=1
        
    result+=s
    m-=1

print(result)
