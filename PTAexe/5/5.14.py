T = int(input())
for _ in range(T):
    n = int(input())
    students = []
    for _ in range(n):
        name, progress, problems = input().split()
        students.append((name, int(progress), int(problems)))
    students.sort(key=lambda x: (-x[1], -x[2], x[0]))
    rank = 1
    for i, student in enumerate(students):
        if i > 0 and student[1:] != students[i-1][1:]:
            rank = i+1
        print(f"{rank} {student[0]} {student[1]} {student[2]}")
