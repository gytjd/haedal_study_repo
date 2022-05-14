#[권희정] 왕실의 나이트

n=input()
r=int(n[1])
#아스키코드로 변환
c=int(ord(n[0]))-int(ord('a'))+1

step=[(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]

cnt=0
for i in step:
    next_r=r+i[0]
    next_c=c+i[1]

    if next_r>0 and next_r<9 and next_c>0 and next_c<9:
        cnt+=1

print(cnt)
