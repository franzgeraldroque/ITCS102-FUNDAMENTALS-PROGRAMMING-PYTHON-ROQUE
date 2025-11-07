def greeter(name):
    print(f"Hi {name}, kamusta ka na?")

def summation(x):
    sum = 0
    for i in range (x,0,-1):
        sum += i
    print(f"The sum of {x} is {sum}")

greeter("Sofia")
greeter("Diaz")
greeter("Nista")
summation(18)
summation(11)

