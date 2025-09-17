num = eval(input("Enter a number --> "))
print(f"The multiplication table of {num} is: ")

for i in range(1,11):
    multiply = num * i
    print(f" {num} * {i} = {multiply}") 
