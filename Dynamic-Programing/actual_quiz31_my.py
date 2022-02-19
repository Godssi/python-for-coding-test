t = int(input())  # 테스트 케이스 수

for i in range(t):
    n, m = map(int, input().split())  # n * m 크기의 금광

    # 금광 정보
    array = list(map(int, input().split()))

    # dp 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])  # 리스트 인덱싱을 이용한 것... 이구나!
        index += m

    # 다이나믹 프로그래밍(보텀업 방싱)
    for j in range(1, m):
        for i in range(n):
            if i == 0:  # 왼쪽 위에서 오는 경우
                left_up = 0
            else:
                left_up = dp[i-1][j-1]

            if i == n-1:  # 왼쪽 아래에서 오는 경우
                left_down = 0
            else:
                left_down = dp[i+1][j-1]

            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left, left_down, left_up)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])

    print(result)



