n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

min_value, max_value = max(a), min(b)
if min_value > max_value:
    print(0)
else:
    print(max_value-min_value+1)
