a, b, c = map(int, input().split())
if a == b:
    print(c)
    exit(0)
if b == c:
    print(a)
    exit(0)
if c == a:
    print(b)
    exit(0)
print(0)
