A = [1, 2, 3, 4]
B = [5, 6, 7, 8]

for ai in A:
    for bi in B:
        if ai == 2 and bi == 7:
            print(ai, bi, "break!")
            break
        print(ai, bi)
    else:
        continue
    break
else:
    print("not printed")