a, b, c, d = map(int, input().split())
red = 0
cnt = 0
if b >= c*d:
    print(-1)
    exit(0)

while True:
    a += b
    red += c
    cnt += 1
    if a <= red*d:
        break

print(cnt)
