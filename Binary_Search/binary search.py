array = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


def binary_search(array, target, start, end):
    if start > end:
        return None

    middle = (start + end) // 2
    if array[middle] == target:
        return middle
    elif array[middle] > target:
        return binary_search(array, target, start, middle-1)
    else:
        return binary_search(array, target, middle+1, end)


n = len(array)
target = int(input())
result = binary_search(array, target, 0, n-1)

if result is None:
    print("원소가 존재하지 않습니다")
else:
    print(result+1)