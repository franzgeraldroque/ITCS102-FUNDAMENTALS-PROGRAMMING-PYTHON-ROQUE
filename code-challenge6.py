number = eval(input("Enter a number --> "))
factorial = 1
for i in range(number, 0, -1):
    factorial1 = factorial
    factorial *= i
    print(factorial1, "*", i, "=", factorial)
print("The factorial is", factorial)