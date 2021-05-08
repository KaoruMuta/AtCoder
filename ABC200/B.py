n, k = map(int, input().split())
for _ in range(k):
    if n % 200 == 0:
        n = n // 200
    else:
        str_n = str(n) + '200'
        n = int(str_n)

print(n)