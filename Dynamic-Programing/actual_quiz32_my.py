n = int(input())  # n: 삼각형의 밑변의 크기

array = []

for i in range(n):
    array.append(list(map(int, input().split())))

# dp 테이블 초기화 및 다이나믹 프로그래밍(보텀업 방식)
dp = array
for i in range(1, n):  # 각 행 마다 진행해야 하므로
    for j in range(i+1):
        if j == 0:  # 대각선 왼쪽의 경우(왼쪽 위에서 내려오는 경우)
            left_up = 0
        else:
            left_up = dp[i-1][j-1]

        if j == i:  # 대각선 오른쪽의 경우(바로 위에서 내려오는 경우)
            right_up = 0
        else:
            right_up = dp[i-1][j]

        dp[i][j] = max(left_up, right_up) + dp[i][j]

result = max(dp[n-1])

print(result)