# 이진 탐색을 사용하여서 풀이 진행
# 항상 주의 이진 탐색을 이용해서 문제를 풀이할 경우 항상 정렬을 먼저 시키자!
n = int(input())  # 가게에 있는 부품의 수
store_list = list(map(int, input().split()))
store_list.sort()

m = int(input())  # 손님이 원하는 부품의 수
guest_list = list(map(int, input().split()))


def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if array[mid] == target:  # 찾은 경우 True 출력
        return True
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


for thing in guest_list:
    if binary_search(store_list, thing, 0, n-1):
        print("yes", end=" ")
    else:
        print("no", end=" ")
