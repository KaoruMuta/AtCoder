n = int(input())
s = list(input())
q = int(input())

is_reversed = False
for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        if is_reversed:
            if a >= n:
                a -= n
            else:
                a += n

            if b >= n:
                b -= n
            else:
                b += n
        s[a-1], s[b-1] = s[b-1], s[a-1]
    elif t == 2:
        is_reversed = not is_reversed

if is_reversed:
    s = s[n:] + s[0:n]
print(''.join(s))
