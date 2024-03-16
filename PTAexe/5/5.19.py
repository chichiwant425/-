while True:
    try:
        n = int(input())
        students = []
        for _ in range(n):
            info = input().split()
            name = info[0]
            scores = list(map(int, info[1:]))
            avg_score = sum(scores) / 3.0
            students.append((name, scores, avg_score))
        students.sort(key=lambda x: (-x[2], x[0]))
        for student in students:
            name, scores, avg_score = student
            print(name, *scores, "{:.2f}".format(avg_score))
    except EOFError:
        break
