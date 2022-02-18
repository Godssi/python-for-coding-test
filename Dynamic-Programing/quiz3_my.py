n = int(input())  # 창고의 개수

food_list = list(map(int, input().split()))  # 창고의 식량량

result = 0
for i in range(n):
    for j in range(i+2,n):
        now_result = 0
        now_result += food_list[i] + food_list[j]

        if result < now_result:
            result = now_result


print(result)
