n = int(input())
a = list(map(int, input().split()))
a = sorted(a)

for idx, val in enumerate(a):
    if idx+1 != val:
        print('No')
        exit(0)

print('Yes')
