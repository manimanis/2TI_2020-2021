for i in range(10000, 100000):
    ni = int(str(i)[::-1])
    if ni > i and ni % i == 0:
        print(i, '*', ni // i, '=', ni)
