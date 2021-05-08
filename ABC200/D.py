# 解説のC++実装をPythonに書き換えた
n = int(input())
a = list(map(int, input().split()))

# リストを200個用意
bk = [[] for _ in range(200)]
# N>=8以上は必ず該当の答えがあるため、累乗の数を絞ることが可能（鳩の巣原理）
count = min(n, 8)

# bit全探索
for i in range(1, 1<<count):
    sig = 0
    s = []
    for j in range(count):
        if i & (1<<j):
            s.append(j + 1)
            sig += a[j]
            sig %= 200
    if len(bk[sig]) != 0:
        print('Yes')
        print(' '.join(map(str, bk[sig])))
        print(' '.join(map(str, s)))
        exit(0)
    else:
        bk[sig] = s

print('No')