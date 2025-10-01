# Diamond
for s in range(1, 4, 1):
    for x in range(1,4,1):
        print(" ", end=" ")
    for o in range(3, s, -1):
        print(" ", end=" ")
    for f in range(1, s, 1):
        print("*", end=" ")
    for i in range(0, s, 1):
        print("*", end=" ")
    print()
for s in range(1, 3, 1):
    for x in range(1,4,1):
        print(" ", end=" ")
    for o in range(0, s, 1):
        print(" ", end=" ")
    for f in range(2, s, -1):
        print("*", end=" ")
    for i in range(3, s, -1):
        print("*", end=" ")
    print()
#Triangles
for s in range(1, 7, 1):
    for o in range(6, s, -1):
        print(" ", end=" ")
    for f in range(1, s, 1):
        print("*", end=" ")
    for i in range(0, s, 1):
        print("*", end=" ")
    print()
for s in range(1, 7, 1):
    for o in range(6, s, -1):
        print(" ", end=" ")
    for f in range(1, s, 1):
        print("*", end=" ")
    for i in range(0, s, 1):
        print("*", end=" ")
    print()
for s in range(1, 7, 1):
    for o in range(6, s, -1):
        print(" ", end=" ")
    for f in range(1, s, 1):
        print("*", end=" ")
    for i in range(0, s, 1):
        print("*", end=" ")
    print()
#Trunk
for s in range(5):
    for o in range(4):
        print(" ", end= " ")
    print("*", end= " ")
    print("*", end= " ")
    print("*", end= " ")
    print()