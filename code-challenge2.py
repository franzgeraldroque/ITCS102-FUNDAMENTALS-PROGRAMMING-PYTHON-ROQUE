amount = eval(input("Enter amount to deposit :"))

denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 1]


print("\nHere is a breakdown in PH denomination: ")

for denom in denominations:
    count = amount // denom
    amount = amount % denom
    print(count, "-", denom)

text = input("\nSana lahat ng tao ganito... ")


