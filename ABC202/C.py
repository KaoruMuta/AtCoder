from collections import Counter

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

b_and_c = []
for idx in c:
    b_and_c.append(b[idx-1])

counter_a = Counter(a)
counter_b_and_c = Counter(b_and_c)
answer = 0

for key, value in counter_b_and_c.items():
    if key in counter_a:
        answer += counter_a[key] * counter_b_and_c[key]

print(answer)