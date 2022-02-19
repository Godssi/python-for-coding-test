array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i  # 가장 작은 원소가 위치할 인덱스
    for j in range(i+1, len(array)):  # 선형 탐색해서 가장 작은 원소를 찾는 반복문
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]  # 스와프 구문

print(array)