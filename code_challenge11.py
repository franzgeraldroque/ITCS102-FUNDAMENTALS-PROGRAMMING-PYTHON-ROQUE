# print("\t\t *", end=" ")
for s in range(1, 12, 1):
    for o in range(11, s, -1):
        print(" ", end=" ")
    for f in range(1, s, 1):
        print("*", end=" ")
    for i in range(0, s, 1):
        print("*", end=" ")
    print()
for s in range(1, 12, 1):
    for o in range(0, s, 1):
        print(" ", end=" ")
    for f in range(10, s, -1):
        print("*", end=" ")
    for i in range(11, s, -1):
        print("*", end=" ")
    print()
# print("\t\t *", end="")