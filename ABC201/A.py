a = list(map(int, input().split()))
a = sorted(a)
if a[0]+a[2] == 2*a[1]:
    print('Yes')
else:
    print('No')
