n, k = map(int, input().split())
a = list(map(int, input().split()))

same_snack_count = k // n
k = k % n
snack = [same_snack_count for _ in range(n)]

sorted_a = sorted((e, i) for i, e in enumerate(a))

for i in range(k):
    target_idx = sorted_a[i][1]
    snack[target_idx] += 1

for s in snack:
    print(s)
