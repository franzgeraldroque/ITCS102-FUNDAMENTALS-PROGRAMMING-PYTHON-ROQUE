for i in range(1, 7, 1):
    for x in range(7, i, -1):
        print(" ", end=" ")
    for f in range(i, 0, -1):
        print(f, end=" ")
    for e in range(2, i + 1, 1):
        print(e, end=" ")
    print()