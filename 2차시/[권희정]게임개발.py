#[권희정]게임 개발
n,m=map(int,input().split())
x,y,direction = map(int, input().split())
#0으로 초기화,방문위치
d=[[0]*m for _ in range(n)]
#map정보
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

arr = [[0 for _ in range(m)] for _ in range(n)]
dx=[-1,0,1,0] #북동남서
dy=[0,1,0,1]
d[x][y]=1 #방문 표시

def turn_left():
    global direction
    direction-=1
    if direction==-1:
        direction=3


cnt=1
turn_cnt = 0

while True:

    turn_left()
    nx=x+dx[direction]
    ny=y+dy[direction]

    #가보지 않았던 칸
    if d[nx][ny]==0 and arr[nx][ny]==0:
        d[nx][ny]=1
        x=nx
        y=ny
        cnt+=1
        turn_cnt=0
        continue

    #바다 or 다 갔는 칸인 경우
    else:
        turn_cnt+=1

    #움직일 수 없는 경우
    if turn_cnt==4:
        nx=x-dx[direction]
        ny=y-dy[direction]

        #뒤로 가기
        if arr[nx][ny]==0:
            x=nx
            y=ny
        #뒤로도 이동x=>바다
        else:
            break
        turn_cnt=0

print(cnt)
    
