def tries(binf, bsup, n):
    tries = 0
    while True:
        tries += 1
        mid = (binf + bsup) // 2
        if mid < n:
            binf = mid + 1
        elif mid > n:
            bsup = mid - 1
        else:
            return tries


MIN, MAX = 1, 127
tdic = {}
for i in range(MIN, MAX+1):
    t = tries(MIN, MAX, i)
    if t not in tdic:
        tdic[t] = []
    tdic[t].append(i)

for i in sorted(tdic.keys()):
    print(i, len(tdic[i]), tdic[i])
