n, m = map(int, input().split())  # n : 화폐의 종류, m : 만들어야하는 화폐의 가치

coin_list = []
for i in range(n):
    coin_list.append(int(input()))

d = [10001] * (m+1) # 1원 ~ m원 까지 최소한의 개수 파악  10001은 만들 수 없는 값 표시
d[0] = 0

# 화폐의 종류별로 파악
for i in range(n):
    for j in range(coin_list[i], m+1):
        if d[j-coin_list[i]] != 10001:
            d[j] = min(d[j], d[j-coin_list[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])




