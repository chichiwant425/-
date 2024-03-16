T = int(input())
for _ in range(T):
    n = int(input())
    scores = {}
    for _ in range(n*(n-1)//2):
        a, b, f = input().split()
        if a not in scores:
            scores[a] = 0
        if b not in scores:
            scores[b] = 0
        if f == '1':
            scores[a] += 3
        elif f == '0':
            scores[a] += 1
            scores[b] += 1
    sorted_scores = sorted(scores.items(), key=lambda x: (-x[1], x[0]))
    max_score = sorted_scores[0][1]
    rank = 1
    result = []
    result.append(f"{rank} {sorted_scores[0][0]}")
    for i in range(1, len(sorted_scores)):
        if sorted_scores[i][1] == max_score:
            result.append(sorted_scores[i][0])
        else:
            max_score = sorted_scores[i][1]
            rank = i + 1
            print(' '.join(result))
            result = []
            result.append(f"{rank} {sorted_scores[i][0]}")
    print(' '.join(result))