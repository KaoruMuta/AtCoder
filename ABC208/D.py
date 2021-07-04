import math
n, m = map(int, input().split())
A, B, C = [], [], []
dis = [[1 << 60] * n for i in range(n)]
for i in range(n):
    dis[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    dis[a-1][b-1] = c

answer = 0
for k in range(n):
    next = [[0] * n for _ in range(n)]
    for t in range(n):
        for s in range(n):
            next[t][s] = min(dis[t][s], dis[t][k]+dis[k][s])
            if next[t][s] < 1 << 59:
                answer += next[t][s]
    dis = next

print(answer)
