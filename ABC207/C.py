n = int(input())
T = []
L = []
R = []
for _ in range(n):
    t, l, r = map(int, input().split())
    T.append(t)
    L.append(l)
    R.append(r)

cnt = 0
for i in range(n-1):
    for j in range(i+1, n):
        first_t, first_l, first_r = T[i], L[i], R[i]
        second_t, second_l, second_r = T[j], L[j], R[j]
        if first_r < second_r:
            val = first_r - second_l
            if val < 0:
                continue
            elif val == 0:
                if (first_t == 1 and second_t == 1) or (first_t == 1 and second_t == 2) or (first_t == 3 and second_t == 1) or (first_t == 3 and second_t == 2):
                    cnt += 1
            else:
                cnt += 1
        else:
            val = second_r - first_l
            if val < 0:
                continue
            elif val == 0:
                if (first_t == 1 and second_t == 1) or (first_t == 2 and second_t == 1) or (first_t == 1 and second_t == 3) or (first_t == 2 and second_t == 3):
                    cnt += 1
            else:
                cnt += 1

print(cnt)
