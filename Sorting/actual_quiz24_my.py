n = int(input())  # 집의 개수

houses = list(map(int, input().split()))
houses.sort()

print(houses[(n-1) // 2])


