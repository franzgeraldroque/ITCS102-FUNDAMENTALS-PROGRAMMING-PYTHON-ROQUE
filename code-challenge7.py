print("ODD NUMBER SUMMATION")
print("Maglagay ng sampong numero")

odd = 0
for i in range(10):
    number = eval(input("ilagay mo ang numero -->"))
    if number %2 != 0:
        odd += number
    else:
        print("ang numero", number, "ay hindi odd number")
print("ang kabuuan ng pangkalahatang odd number ay", odd)