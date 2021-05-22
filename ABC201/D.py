import math

h, w = map(int, input().split())
a = [[(1 if i == '+' else -1) for i in input()] for _ in range(h)]

dp = [[-math.inf for _ in range(w)] for _ in range(h)]
# 最後を0
dp[-1][-1] = 0

for i in reversed(range(h)):
    for j in reversed(range(w)):
        if i+1 < h:
            dp[i][j] = max(dp[i][j], a[i+1][j]-dp[i+1][j])
        if j+1 < w:
            dp[i][j] = max(dp[i][j], a[i][j+1]-dp[i][j+1])

if dp[0][0] > 0:
    print('Takahashi')
elif dp[0][0] == 0:
    print('Draw')
else:
    print('Aoki')
