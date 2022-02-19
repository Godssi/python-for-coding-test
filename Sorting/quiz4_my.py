n, k = map(int, input().split())

num_list1 = list(map(int, input().split()))

num_list2 = list(map(int, input().split()))

# 풀이 : num_list1 은 오름차순으로 num_list2는 내림차순으로 정렬한 다음 앞의 원소 k 개 만큼을 바꿔주면 된다.

num_list1.sort()
num_list2.sort(reverse=True)

for i in range(k):
    if num_list1[i] < num_list2[i]:
        num_list1[i], num_list2[i] = num_list2[i], num_list1[i]
    else:  # num_list1 의 원소가  num_list2 의 원소보다 크거나 같을 때, 반복문 탈출
        break

print(sum(num_list1))