#숫자 카드 게임

n,m=map(int,input().split())
result=0

for i in range(n):
    data=list(map(int,input().split()))
    min_num=min(data)
    
    if result<min_num:
        result=min_num

print(result)
