n = int(input())  # 학생의 수

scores = [tuple(input().split()) for _ in range(n)]

scores.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in scores:
    print(student[0])