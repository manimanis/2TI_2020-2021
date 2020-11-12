for i in range(100, 999):
    u = i % 10
    d = (i // 10) % 10
    c = i // 100
    ii = int(str(i)[::-1])
    if u+d+c == 9 and i-99 == ii:
        print(i, '-', 99, '=', ii)
