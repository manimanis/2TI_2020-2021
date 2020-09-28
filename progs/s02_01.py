from random import randint, seed

seed(892012)

l = []
while True:
    v = randint(10, 99)
    if (v not in l) or l[0] != v:
        l.append(v)
    else:
        l1 = [v]
        while True:
            v1 = randint(10, 99)
            if len(l) > len(l1) and l[len(l1)] == v1:
                l1.append(v1)
            elif len(l) == len(l1):
                break
            else:
                l1.append(v1)
                l = l + l1
                break
        if len(l) == len(l1):
            print(len(l), l)
            break
    if len(l) % 1000 == 0:
        print(len(l))
