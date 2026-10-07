# 공간의 크기 N 입력
n = int(input())
# 2. 이동할 계획(L, R, U, D) 입력
plans = input().split()

# 시작 좌표 설정 (문제 주어짐)
x, y = 1, 1

# L(좌), R(우), U(상), D(하)에 따른 이동 방향 설정 
# (2차원 배열시 x는 행(위아래), y는 열(좌우)을 의미)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 계획서에 적힌 명령을 하나씩 확인하며 이동
for plan in plans:
    # 어떤 방향으로 이동하는지 확인하고, 다음 위치(nx, ny) 임시 계산
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            
    # 공간을 벗어나는 경우 (지도를 벗어나면) 무시하고 다음 명령으로 넘어감
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
        
    # 정상적인 이동이라면 실제 내 위치(x, y)를 임시 위치(nx, ny)로 업데이트
    x, y = nx, ny

# 최종 좌표 출력
print(x, y)
