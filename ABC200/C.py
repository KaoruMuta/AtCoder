import collections

n = int(input())
a = list(map(int, input().split()))
answer = 0

for i in range(n):
    a[i] %= 200

mod_collection = collections.Counter(a)
for count in mod_collection.values():
    answer += count * (count-1) // 2

print(answer)
