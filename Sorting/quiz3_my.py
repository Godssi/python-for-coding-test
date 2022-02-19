n = int(input())  # 학생 수

# 학생 점수 정보 입력받음
std_score = []
for i in range(n):
    name, score = input().split()
    std_score.append((name, score))

std_score = sorted(std_score, key=lambda student: student[1])

for student in std_score:
    print(student[0], end=' ')
