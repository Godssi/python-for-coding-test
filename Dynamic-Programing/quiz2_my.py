x = int(input())

d = [0] * 30001  # d : 그 수로부터 1 까지 만드는데 걸리는 연산 횟수

for i in range(2, x+1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1

    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)

    print(i, d[i])

print(d[x])