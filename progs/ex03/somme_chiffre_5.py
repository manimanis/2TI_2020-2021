for i in range(10, 99):
    d = i // 10
    u = i % 10
    if (d + u) % 5 == 0:
        print(i)
