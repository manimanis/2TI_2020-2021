for i in range(10, 100):
    for j in range(i, 100):
        p = i * j
        if p >= 1000 and p % 100 == 91:
            print(i, '*', j, '=', p)
